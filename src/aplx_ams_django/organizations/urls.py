"""
FEAT-002 stub: organizations URL configuration.

urlpatterns is empty in Mode A so that every API call returns 404 (the
correct red-run failure). The router registration is added in Mode B
(FEAT-002) once the viewsets have their full implementation.
"""

from django.urls import URLPattern

urlpatterns: list[URLPattern] = []
