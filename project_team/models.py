from django.db import models
from accounts.models import CustomUser
from projects.models import Project

class ProjectTeamMember(models.Model):
    ROLE_CHOICES = [
        ("PROJECT_MANAGER", "Project Manager"),
        ("ENGINEER", "Engineer"),
        ("SUPERVISOR", "Supervisor"),
        ("ACCOUNTANT", "Accountant"),
        ("WORKER", "Worker"),
        ("OTHER", "Other"),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="team_members")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="project_assignments")
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default="OTHER")
    is_active = models.BooleanField(default=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["project", "user"], name="unique_project_team_member")]
        ordering = ["-assigned_at"]

    def __str__(self):
        return f"{self.project.project_name} - {self.user.username}"
