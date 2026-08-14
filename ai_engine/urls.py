
from django.urls import path

from .views import (
    ProjectRiskView,
    ProjectCostRiskView,
    MaterialStockView,
    LabourRequirementView,
    DelayPredictionView,
    MaterialRequirementView,
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
    path(
        "labour-requirement/<int:project_id>/",
        LabourRequirementView.as_view(),
    ),
    path(
    "delay-risk/<int:project_id>/",
    DelayPredictionView.as_view(),
    ),
    path(
    "material-requirement/<int:project_id>/",
    MaterialRequirementView.as_view(),
    ),
]