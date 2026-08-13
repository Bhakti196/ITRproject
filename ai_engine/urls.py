from django.urls import path

from .views import (
    ProjectRiskView,
    ProjectCostRiskView,
    MaterialStockView,
)


urlpatterns = [
    path(
        "project-risk/<int:project_id>/",
        ProjectRiskView.as_view(),
    ),
    path(
        "project-cost-risk/<int:project_id>/",
        ProjectCostRiskView.as_view(),
    ),
    path(
        "material-stock/<int:project_id>/",
        MaterialStockView.as_view(),
    ),
]