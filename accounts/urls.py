from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),

    # Login
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # Refresh Access Token
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]