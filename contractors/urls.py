from django.urls import path
from .views import ContractorListCreateView, contractor_detail

urlpatterns = [
    path("", ContractorListCreateView.as_view(), name="contractors"),
    path("<int:pk>/", contractor_detail, name="contractor_detail"),
]