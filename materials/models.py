from django.db import models
from projects.models import Project
from accounts.models import CustomUser


class Material(models.Model):

    UNIT_CHOICES = [
        ("KG", "Kilogram"),
        ("TON", "Ton"),
        ("BAG", "Bag"),
        ("M3", "Cubic Meter"),
        ("LITRE", "Litre"),
        ("PIECE", "Piece"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="materials"
    )

    material_name = models.CharField(max_length=200)

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit = models.CharField(
        max_length=20,
        choices=UNIT_CHOICES
    )

    minimum_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.material_name


class InventoryTransaction(models.Model):

    TRANSACTION_TYPES = [
        ("RECEIVE", "Receive"),
        ("ISSUE", "Issue"),
        ("CONSUME", "Consume"),
    ]

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    notes = models.TextField(
        blank=True
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.material.material_name} - "
            f"{self.transaction_type} - "
            f"{self.quantity}"
        )