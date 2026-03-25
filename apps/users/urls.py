# apps/users/urls.py

from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r"utilizadores", UserViewSet, basename="utilizadores")

urlpatterns = router.urls
