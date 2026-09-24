from django.db import models
from accounts.models import CustomUser
from sites.models import Site
from tasks.models import Task


class Labour(models.Model):

    worker_name = models.CharField(max_length=200)

    role = models.CharField(max_length=100)

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name="labour_records"
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    attendance_date = models.DateField()

    hours_worked = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    daily_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.worker_name} - {self.role}"