from django.urls import path
from .views import ContractorListCreateView

urlpatterns = [
    path("", ContractorListCreateView.as_view(), name="contractors"),
]