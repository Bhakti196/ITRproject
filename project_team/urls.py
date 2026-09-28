from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProjectTeamMemberViewSet

router = DefaultRouter()
router.register("members", ProjectTeamMemberViewSet, basename="project-team-member")
urlpatterns = [path("", include(router.urls))]
