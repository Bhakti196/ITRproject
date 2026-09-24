from django.urls import path
from .views import LabourListCreateView

urlpatterns = [
    path("", LabourListCreateView.as_view(), name="labour"),
]