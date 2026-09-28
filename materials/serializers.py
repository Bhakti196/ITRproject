from rest_framework import serializers

from .models import Material, InventoryTransaction


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]


class InventoryTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryTransaction
        fields = "__all__"
        read_only_fields = [
            "created_by",
            "created_at",
        ]