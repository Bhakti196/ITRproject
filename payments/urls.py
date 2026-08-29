from django.urls import path

from .views import PaymentListCreateView, payment_detail


urlpatterns = [
    path("", PaymentListCreateView.as_view(), name="payments"),
    path("<int:pk>/", payment_detail, name="payment-detail"),
]