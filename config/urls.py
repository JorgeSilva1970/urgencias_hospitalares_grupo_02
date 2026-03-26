# config/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Autenticação JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Rotas por módulo
    path("api/pacientes/", include("apps.pacientes.urls")),
    path("api/episodios/", include("apps.episodios.urls")),
    path("api/internamentos/", include("apps.internamentos.urls")),
    path("api/exames/", include("apps.exames.urls")),
    path("api/faturacao/", include("apps.faturacao.urls")),
    path("api/users/", include("apps.users.urls")),
]