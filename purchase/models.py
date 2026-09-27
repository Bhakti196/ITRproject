from django.db import models
from projects.models import Project
from accounts.models import CustomUser


class Purchase(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("ORDERED", "Ordered"),
        ("RECEIVED", "Received"),
        ("CANCELLED", "Cancelled"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="purchases"
    )

    supplier_name = models.CharField(max_length=200)

    purchase_number = models.CharField(
        max_length=100,
        unique=True
    )

    purchase_date = models.DateField()

    item_name = models.CharField(max_length=200)

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit = models.CharField(max_length=30)

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    total_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.purchase_number} - {self.item_name}"
