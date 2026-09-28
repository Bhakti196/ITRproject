from django.db import models
from accounts.models import CustomUser
from projects.models import Project

class Incident(models.Model):
    SEVERITY_CHOICES = [("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High"), ("CRITICAL", "Critical")]
    STATUS_CHOICES = [("OPEN", "Open"), ("INVESTIGATING", "Investigating"), ("RESOLVED", "Resolved"), ("CLOSED", "Closed")]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="incidents")
    incident_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=300, blank=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default="MEDIUM")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
    reported_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="reported_incidents")
    corrective_action = models.TextField(blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-incident_date", "-created_at"]

    def __str__(self):
        return self.title
