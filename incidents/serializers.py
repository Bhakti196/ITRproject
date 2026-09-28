from rest_framework import serializers
from .models import Incident
class IncidentSerializer(serializers.ModelSerializer):
    reported_by_name = serializers.CharField(source="reported_by.full_name", read_only=True)
    project_name = serializers.CharField(source="project.project_name", read_only=True)
    class Meta:
        model = Incident
        fields = "__all__"
        read_only_fields = ["reported_by", "created_at"]
