# apps/faturacao/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    FaturacaoViewSet,
    monitorizacao_administrativa,
    monitorizacao_administrativa_anonimizada,
    exportar_monitorizacao_json,
    exportar_monitorizacao_csv,
)

router = DefaultRouter()
router.register(r"faturacao", FaturacaoViewSet, basename="faturacao")

urlpatterns = router.urls + [
    path(
        "monitorizacao-administrativa/<int:utente_id>/",
        monitorizacao_administrativa,
        name="monitorizacao-administrativa",
    ),
    path(
        "monitorizacao-administrativa-anonimizada/<int:utente_id>/",
        monitorizacao_administrativa_anonimizada,
        name="monitorizacao-administrativa-anonimizada",
    ),
    path(
        "exportar-json/<int:utente_id>/",
        exportar_monitorizacao_json,
        name="exportar-monitorizacao-json",
    ),
    path(
        "exportar-csv/<int:utente_id>/",
        exportar_monitorizacao_csv,
        name="exportar-monitorizacao-csv",
    ),
]