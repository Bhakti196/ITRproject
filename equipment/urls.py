from django.urls import path
from .views import EquipmentListCreateView

urlpatterns = [
    path("", EquipmentListCreateView.as_view(), name="equipment"),
]