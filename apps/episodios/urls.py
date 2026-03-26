# apps/episodios/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    HospitalViewSet,
    EpisodioUrgenciaViewSet,
    TriagemViewSet,
    ConsultaViewSet,
    PrescricaoViewSet,
    painel_triagem,
)

router = DefaultRouter()
router.register(r"hospitais", HospitalViewSet, basename="hospitais")
router.register(r"episodios", EpisodioUrgenciaViewSet, basename="episodios")
router.register(r"triagens", TriagemViewSet, basename="triagens")
router.register(r"consultas", ConsultaViewSet, basename="consultas")
router.register(r"prescricoes", PrescricaoViewSet, basename="prescricoes")

urlpatterns = router.urls + [
    path("painel-triagem/", painel_triagem, name="painel-triagem"),
]