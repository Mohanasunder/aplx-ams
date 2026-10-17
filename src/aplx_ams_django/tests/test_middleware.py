"""Unit tests for APLX AMS middleware classes."""

import time

from django.http import HttpRequest, HttpResponse
from django.test import RequestFactory

from aplx_ams_django.middleware import (
    _ABSOLUTE_TIMEOUT_SECONDS,
    _IDLE_TIMEOUT_SECONDS,
    AbsoluteSessionTimeoutMiddleware,
    RLSContextMiddleware,
    SecurityHeadersMiddleware,
)


def _get_response(request: HttpRequest) -> HttpResponse:
    return HttpResponse("ok")


class _MockUser:
    def __init__(
        self, authenticated: bool, role: str | None = None, org_id: int | None = None
    ) -> None:
        self.is_authenticated = authenticated
        self.role = role
        self.org_id = org_id


class _MockSession(dict[str, object]):
    def flush(self) -> None:
        self.clear()


class TestRLSContextMiddleware:
    def _make_request(
        self, authenticated: bool, role: str | None = None, org_id: int | None = None
    ) -> HttpRequest:
        rf = RequestFactory()
        request = rf.get("/")
        request.user = _MockUser(authenticated, role=role, org_id=org_id)
        return request

    def test_authenticated_user_sets_rls_context(self) -> None:
        mw = RLSContextMiddleware(_get_response)
        request = self._make_request(True, role="L1", org_id=42)
        mw(request)
        assert request.rls_user_kind == "L1"
        assert request.rls_org_id == 42

    def test_anonymous_user_sets_rls_context_to_none(self) -> None:
        mw = RLSContextMiddleware(_get_response)
        request = self._make_request(False)
        mw(request)
        assert request.rls_user_kind is None
        assert request.rls_org_id is None

    def test_authenticated_user_without_role_sets_none(self) -> None:
        mw = RLSContextMiddleware(_get_response)
        request = self._make_request(True)
        mw(request)
        assert request.rls_user_kind is None
        assert request.rls_org_id is None


class TestAbsoluteSessionTimeoutMiddleware:
    def _make_request(
        self, authenticated: bool, session: dict[str, object] | None = None
    ) -> HttpRequest:
        rf = RequestFactory()
        request = rf.get("/")
        request.user = _MockUser(authenticated)
        request.session = _MockSession(session or {})
        return request

    def test_anonymous_user_passes_through(self) -> None:
        mw = AbsoluteSessionTimeoutMiddleware(_get_response)
        request = self._make_request(False)
        response = mw(request)
        assert response.status_code == 200

    def test_authenticated_no_session_data_passes_and_sets_activity(self) -> None:
        mw = AbsoluteSessionTimeoutMiddleware(_get_response)
        request = self._make_request(True, {})
        response = mw(request)
        assert response.status_code == 200
        assert "last_activity" in request.session

    def test_authenticated_recent_activity_passes(self) -> None:
        mw = AbsoluteSessionTimeoutMiddleware(_get_response)
        now = int(time.time())
        request = self._make_request(True, {"last_activity": now - 60, "session_start": now - 600})
        response = mw(request)
        assert response.status_code == 200

    def test_idle_timeout_returns_401(self) -> None:
        mw = AbsoluteSessionTimeoutMiddleware(_get_response)
        now = int(time.time())
        expired = now - _IDLE_TIMEOUT_SECONDS - 1
        request = self._make_request(True, {"last_activity": expired})
        response = mw(request)
        assert response.status_code == 401

    def test_absolute_timeout_returns_401(self) -> None:
        mw = AbsoluteSessionTimeoutMiddleware(_get_response)
        now = int(time.time())
        old_start = now - _ABSOLUTE_TIMEOUT_SECONDS - 1
        request = self._make_request(True, {"last_activity": now - 60, "session_start": old_start})
        response = mw(request)
        assert response.status_code == 401

    def test_idle_timeout_flushes_session(self) -> None:
        mw = AbsoluteSessionTimeoutMiddleware(_get_response)
        now = int(time.time())
        expired = now - _IDLE_TIMEOUT_SECONDS - 1
        request = self._make_request(True, {"last_activity": expired, "session_start": now - 60})
        mw(request)
        assert len(request.session) == 0


class TestSecurityHeadersMiddleware:
    def _make_request(self) -> HttpRequest:
        rf = RequestFactory()
        return rf.get("/")

    def test_csp_header_set(self) -> None:
        mw = SecurityHeadersMiddleware(_get_response)
        response = mw(self._make_request())
        csp = response["Content-Security-Policy"]
        assert "default-src 'self'" in csp
        assert "frame-ancestors 'none'" in csp

    def test_x_frame_options_deny(self) -> None:
        mw = SecurityHeadersMiddleware(_get_response)
        response = mw(self._make_request())
        assert response["X-Frame-Options"] == "DENY"

    def test_x_content_type_options_nosniff(self) -> None:
        mw = SecurityHeadersMiddleware(_get_response)
        response = mw(self._make_request())
        assert response["X-Content-Type-Options"] == "nosniff"

    def test_referrer_policy_no_referrer(self) -> None:
        mw = SecurityHeadersMiddleware(_get_response)
        response = mw(self._make_request())
        assert response["Referrer-Policy"] == "no-referrer"

    def test_hsts_not_set(self) -> None:
        mw = SecurityHeadersMiddleware(_get_response)
        response = mw(self._make_request())
        assert "Strict-Transport-Security" not in response
