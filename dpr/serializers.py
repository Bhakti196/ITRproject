from rest_framework import serializers
from .models import DailyProgressReport


class DailyProgressReportSerializer(serializers.ModelSerializer):

    task_name = serializers.CharField(
        source="task.task_name",
        read_only=True
    )

    project_id = serializers.IntegerField(
        source="task.project.id",
        read_only=True
    )

    project_name = serializers.CharField(
        source="task.project.project_name",
        read_only=True
    )

    class Meta:
        model = DailyProgressReport
        fields = "__all__"
        read_only_fields = [
            "created_by",
            "created_at",
            "task_name",
            "project_id",
            "project_name",
        ]