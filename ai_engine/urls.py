
from django.urls import path

from .views import (
    ProjectRiskView,
    ProjectCostRiskView,
    MaterialStockView,
    LabourRequirementView,
    DelayPredictionView,
    MaterialRequirementView,
    DPRProgressAnalysisView,
    ProgressReportView,
    SafetyRiskView,
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
    "dpr-progress/<int:project_id>/",
    DPRProgressAnalysisView.as_view(),
    ),
    path(
    "material-requirement/<int:project_id>/",
    MaterialRequirementView.as_view(),
    ),
    path(
    "delay-prediction/<int:project_id>/",
    DelayPredictionView.as_view(),
    ),
    path(
    "progress-report/<int:project_id>/",
    ProgressReportView.as_view(),
    ),
    path(
    "safety-risk/<int:project_id>/",
    SafetyRiskView.as_view(),
    ),
]