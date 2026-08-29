from django.db import models
from accounts.models import CustomUser
from sites.models import Site


class Equipment(models.Model):

    STATUS_CHOICES = [
        ("AVAILABLE", "Available"),
        ("IN_USE", "In Use"),
        ("MAINTENANCE", "Maintenance"),
    ]

    equipment_name = models.CharField(max_length=200)

    equipment_type = models.CharField(max_length=100)

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name="equipment"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="AVAILABLE"
    )

    operator_name = models.CharField(
        max_length=200,
        blank=True
    )

    daily_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    last_maintenance = models.DateField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.equipment_name