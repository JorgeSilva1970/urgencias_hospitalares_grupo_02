# apps/internamentos/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    InternamentoViewSet,
    ResumoDiarioInternamentoViewSet,
    consultar_utente_internado,
)

router = DefaultRouter()
router.register(r"internamentos", InternamentoViewSet, basename="internamentos")
router.register(r"resumos-diarios", ResumoDiarioInternamentoViewSet, basename="resumos-diarios")

urlpatterns = router.urls + [
    path(
        "consultar-utente-internado/<int:utente_id>/",
        consultar_utente_internado,
        name="consultar-utente-internado",
    ),
]