from rest_framework import serializers
from .models import Contractor


class ContractorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contractor
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]