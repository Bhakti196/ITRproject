from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ProjectTeamMember
from .serializers import ProjectTeamMemberSerializer

class ProjectTeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTeamMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProjectTeamMember.objects.filter(project__created_by=self.request.user).select_related("project", "user")
