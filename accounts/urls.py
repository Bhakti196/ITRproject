from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import LoginView, home
from accounts.user_views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("", home, name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]