from rest_framework import serializers
from .models import Labour


class LabourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Labour
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]