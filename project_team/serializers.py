from rest_framework import serializers
from .models import ProjectTeamMember

class ProjectTeamMemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    full_name = serializers.CharField(source="user.full_name", read_only=True)
    project_name = serializers.CharField(source="project.project_name", read_only=True)

    class Meta:
        model = ProjectTeamMember
        fields = ["id", "project", "project_name", "user", "username", "full_name", "role", "is_active", "assigned_at", "notes"]
        read_only_fields = ["assigned_at"]
