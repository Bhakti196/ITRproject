from rest_framework import serializers
from .models import Estimate, BOQItem

class BOQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOQItem
        fields = "__all__"
        read_only_fields = ["amount"]

class EstimateSerializer(serializers.ModelSerializer):
    items = BOQItemSerializer(many=True, read_only=True)
    total_amount = serializers.DecimalField(max_digits=16, decimal_places=2, read_only=True)
    project_name = serializers.CharField(source="project.project_name", read_only=True)
    class Meta:
        model = Estimate
        fields = "__all__"
        read_only_fields = ["created_by", "created_at", "total_amount"]

class EstimateCreateSerializer(serializers.ModelSerializer):
    items = BOQItemSerializer(many=True, required=False)
    class Meta:
        model = Estimate
        fields = ["project", "estimate_number", "title", "status", "notes", "items"]

    def create(self, validated_data):
        items = validated_data.pop("items", [])
        estimate = Estimate.objects.create(created_by=self.context["request"].user, **validated_data)
        for item in items:
            BOQItem.objects.create(estimate=estimate, **item)
        return estimate
