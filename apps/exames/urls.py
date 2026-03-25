# apps/exames/urls.py

from rest_framework.routers import DefaultRouter
from .views import ExameViewSet

router = DefaultRouter()
router.register(r"exames", ExameViewSet, basename="exames")

urlpatterns = router.urls