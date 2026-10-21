"""
FEAT-010 sla URL configuration.

Holiday endpoints (registered at api/holidays/ in root urls.py by Mode B):
  /api/holidays/        -> HolidayEntryViewSet (list, create)
  /api/holidays/{pk}/   -> HolidayEntryViewSet (destroy)

Mode B backend-builder adds the include() call in src/aplx_ams_django/urls.py.
"""

from rest_framework.routers import DefaultRouter

from aplx_ams_django.sla.views import HolidayEntryViewSet

router = DefaultRouter()
# Empty prefix: this module is mounted at api/holidays/ by the root urlconf.
router.register("", HolidayEntryViewSet, basename="holiday")

urlpatterns = router.urls
