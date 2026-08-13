from django.urls import path
from .views import ProjectRiskView, ProjectCostRiskView

urlpatterns = [
    path("project-risk/<int:project_id>/", ProjectRiskView.as_view()),
    path(
        "project-cost-risk/<int:project_id>/",
        ProjectCostRiskView.as_view()
    ),
]