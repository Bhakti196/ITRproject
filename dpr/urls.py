from django.urls import path

from .views import (
    DPRListCreateView,
    DPRDetailView,
)


urlpatterns = [
    path(
        "",
        DPRListCreateView.as_view(),
        name="dpr"
    ),

    path(
        "<int:pk>/",
        DPRDetailView.as_view(),
        name="dpr_detail"
    ),
]