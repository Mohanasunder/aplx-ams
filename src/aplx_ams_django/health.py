from django.http import HttpRequest, JsonResponse


def health_check(request: HttpRequest) -> JsonResponse:
    """Return {"status": "ok"} with HTTP 200. No auth required (public)."""
    return JsonResponse({"status": "ok"}, status=200)
