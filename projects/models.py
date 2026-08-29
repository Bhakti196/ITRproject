from django.db import models
from accounts.models import CustomUser
from sites.models import Site


class Project(models.Model):

    STATUS_CHOICES = [
        ("NOT_STARTED", "Not Started"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
    ]

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    project_name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    start_date = models.DateField()

    end_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="NOT_STARTED"
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name