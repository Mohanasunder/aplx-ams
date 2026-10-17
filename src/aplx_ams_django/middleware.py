"""
Django middleware for APLX AMS.

Implements three middleware classes per STD-001:
  - RLSContextMiddleware: attaches RLS context (user kind and org) to each request.
  - AbsoluteSessionTimeoutMiddleware: enforces rolling idle (60 min) and absolute (12 h) timeouts.
  - SecurityHeadersMiddleware: adds required HTTP security headers to every response.
"""

import time
from collections.abc import Callable

from django.http import HttpRequest, HttpResponse, JsonResponse


class RLSContextMiddleware:
    """
    Attach the current user's RLS context to the request.

    Sets request.rls_user_kind and request.rls_org_id so the DAL layer
    can apply Row-Level Security without re-querying the user object.
    """

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            request.rls_user_kind = getattr(request.user, "role", None)
            request.rls_org_id = getattr(request.user, "org_id", None)
        else:
            request.rls_user_kind = None
            request.rls_org_id = None
        return self.get_response(request)


_SESSION_EXPIRED_RESPONSE_BODY = {"detail": "Session expired. Please sign in again."}
_IDLE_TIMEOUT_SECONDS = 3600  # 60 minutes
_ABSOLUTE_TIMEOUT_SECONDS = 43200  # 12 hours


class AbsoluteSessionTimeoutMiddleware:
    """
    Enforce session timeouts per STD-001 § Authentication and sessions.

    Two rules apply for authenticated users:
      1. Rolling idle timeout: 60 minutes since last_activity.
      2. Absolute session timeout: 12 hours since session_start.

    On expiry the session is flushed and a 401 JSON response is returned.
    Anonymous requests are passed through without any session checks.
    """

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            return self.get_response(request)

        now = int(time.time())

        last_activity: int | None = request.session.get("last_activity")
        if last_activity is not None and (now - last_activity) > _IDLE_TIMEOUT_SECONDS:
            request.session.flush()
            return JsonResponse(_SESSION_EXPIRED_RESPONSE_BODY, status=401)

        session_start: int | None = request.session.get("session_start")
        if session_start is not None and (now - session_start) > _ABSOLUTE_TIMEOUT_SECONDS:
            request.session.flush()
            return JsonResponse(_SESSION_EXPIRED_RESPONSE_BODY, status=401)

        request.session["last_activity"] = now
        return self.get_response(request)


class SecurityHeadersMiddleware:
    """
    Add required HTTP security headers to every response per STD-001 § HTTP security headers.

    Note: Strict-Transport-Security is intentionally omitted — that header is
    set by Nginx (STD-001 § HTTP security headers, last row).
    """

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        response["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "font-src 'self'; "
            "connect-src 'self'; "
            "frame-ancestors 'none'"
        )
        response["X-Frame-Options"] = "DENY"
        response["X-Content-Type-Options"] = "nosniff"
        response["Referrer-Policy"] = "no-referrer"
        return response
