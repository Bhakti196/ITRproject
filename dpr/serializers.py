from rest_framework import serializers
from .models import DailyProgressReport


class DailyProgressReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyProgressReport
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]