from django.urls import path

from .views import (
    MaterialListCreateView,
    MaterialDetailView,
    material_transactions,
)


urlpatterns = [
    path(
        "",
        MaterialListCreateView.as_view(),
        name="materials"
    ),

    path(
        "<int:pk>/",
        MaterialDetailView.as_view(),
        name="material_detail"
    ),

    path(
        "<int:pk>/transactions/",
        material_transactions,
        name="material_transactions"
    ),
]