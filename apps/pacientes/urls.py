# apps/pacientes/urls.py

from rest_framework.routers import DefaultRouter
from .views import UtenteViewSet

router = DefaultRouter()
router.register(r"utentes", UtenteViewSet, basename="utentes")

urlpatterns = router.urls