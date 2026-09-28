from decimal import Decimal

from django.db import transaction

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Material, InventoryTransaction
from .serializers import (
    MaterialSerializer,
    InventoryTransactionSerializer,
)


class MaterialListCreateView(generics.ListCreateAPIView):

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Material.objects.filter(
            created_by=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
        )


class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Material.objects.filter(
            created_by=self.request.user
        )


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def material_transactions(request, pk):

    try:
        material = Material.objects.get(
            pk=pk,
            created_by=request.user
        )

    except Material.DoesNotExist:
        return Response(
            {"detail": "Material record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET transaction history
    if request.method == "GET":

        transactions = InventoryTransaction.objects.filter(
            material=material,
            created_by=request.user
        ).order_by("-created_at")

        serializer = InventoryTransactionSerializer(
            transactions,
            many=True
        )

        return Response(serializer.data)

    # POST new inventory transaction
    serializer = InventoryTransactionSerializer(
        data=request.data
    )

    if not serializer.is_valid():
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    transaction_type = serializer.validated_data["transaction_type"]
    quantity = serializer.validated_data["quantity"]
    notes = serializer.validated_data.get("notes", "")

    # Quantity must be positive
    if quantity <= Decimal("0"):
        return Response(
            {
                "detail": "Transaction quantity must be greater than zero."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    with transaction.atomic():

        material = Material.objects.select_for_update().get(
            pk=material.pk
        )

        current_stock = material.quantity

        # RECEIVE → increase stock
        if transaction_type == "RECEIVE":

            new_stock = current_stock + quantity

        # ISSUE / CONSUME → decrease stock
        elif transaction_type in ["ISSUE", "CONSUME"]:

            if quantity > current_stock:
                return Response(
                    {
                        "detail": "Insufficient stock.",
                        "current_stock": current_stock,
                        "requested_quantity": quantity,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            new_stock = current_stock - quantity

        else:

            return Response(
                {
                    "detail": "Invalid transaction type."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update current material stock
        material.quantity = new_stock

        material.save(
            update_fields=["quantity"]
        )

        # Save transaction history
        inventory_transaction = InventoryTransaction.objects.create(
            material=material,
            transaction_type=transaction_type,
            quantity=quantity,
            notes=notes,
            created_by=request.user
        )

    return Response(
        {
            "message": "Inventory transaction recorded successfully.",
            "transaction": InventoryTransactionSerializer(
                inventory_transaction
            ).data,
            "previous_stock": current_stock,
            "current_stock": new_stock,
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def material_detail(request, pk):

    try:
        material = Material.objects.get(
            pk=pk,
            created_by=request.user
        )

    except Material.DoesNotExist:
        return Response(
            {"detail": "Material record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    material.delete()

    return Response(
        {"detail": "Material record deleted successfully."},
        status=status.HTTP_204_NO_CONTENT
    )