from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    site_name = serializers.CharField(source="site.site_name", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "site",
            "site_name",
            "project_name",
            "description",
            "start_date",
            "end_date",
            "status",
            "budget",
            "created_by",
            "created_at",
        ]
        read_only_fields = ["created_by", "created_at"]