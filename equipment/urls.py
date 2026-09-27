from django.urls import path

from .views import EquipmentListCreateView, EquipmentDetailView


urlpatterns = [
    path(
        "",
        EquipmentListCreateView.as_view(),
        name="equipment"
    ),

    path(
        "<int:pk>/",
        EquipmentDetailView.as_view(),
        name="equipment_detail"
    ),
]