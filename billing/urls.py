from django.urls import path
from .views import BillingListCreateView, BillingDetailView


urlpatterns = [
    path("", BillingListCreateView.as_view(), name="billing"),
    path("<int:pk>/", BillingDetailView.as_view(), name="billing-detail"),
]