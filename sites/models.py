from django.db import models
from accounts.models import CustomUser


class Site(models.Model):

    STATUS_CHOICES = [
        ("PLANNED", "Planned"),
        ("ONGOING", "Ongoing"),
        ("COMPLETED", "Completed"),
    ]

    site_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PLANNED"
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="sites"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name