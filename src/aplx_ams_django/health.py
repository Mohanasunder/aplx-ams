from django.http import HttpResponse


def health_check(request: object) -> HttpResponse:
    raise NotImplementedError
