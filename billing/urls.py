from django.urls import path
from .views import BillingListCreateView


urlpatterns = [
    path("", BillingListCreateView.as_view(), name="billing"),
]