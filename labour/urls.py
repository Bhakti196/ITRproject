from django.urls import path

from .views import LabourListCreateView, LabourDetailView


urlpatterns = [
    path(
        "",
        LabourListCreateView.as_view(),
        name="labour"
    ),

    path(
        "<int:pk>/",
        LabourDetailView.as_view(),
        name="labour_detail"
    ),
]