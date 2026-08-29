from django.urls import path

from .views import (
    MaterialListCreateView,
    material_detail
)


urlpatterns = [
    path(
        "",
        MaterialListCreateView.as_view(),
        name="materials"
    ),

    path(
        "<int:pk>/",
        material_detail,
        name="material_detail"
    ),
]