from django.urls import path

from .views import ProjectListCreateView, project_detail


urlpatterns = [
    path(
        "",
        ProjectListCreateView.as_view(),
        name="projects"
    ),

    path(
        "<int:pk>/",
        project_detail,
        name="project_detail"
    ),
]