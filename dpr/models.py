from django.db import models
from tasks.models import Task
from accounts.models import CustomUser


class DailyProgressReport(models.Model):

    WEATHER_CHOICES = [
        ("SUNNY", "Sunny"),
        ("CLOUDY", "Cloudy"),
        ("RAINY", "Rainy"),
    ]

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="daily_reports"
    )

    report_date = models.DateField()

    work_done = models.TextField()

    progress_percentage = models.PositiveIntegerField()

    workers_present = models.PositiveIntegerField()

    weather = models.CharField(
        max_length=20,
        choices=WEATHER_CHOICES,
        default="SUNNY"
    )

    remarks = models.TextField(blank=True)

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.task_name} - {self.report_date}"