from django.urls import path
from .views import ProjectRiskView

urlpatterns = [
    path("project-risk/<int:project_id>/", ProjectRiskView.as_view()),
]