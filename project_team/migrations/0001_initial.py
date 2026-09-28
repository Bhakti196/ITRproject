from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0002_Project_budget"),
    ]
    operations = [
        migrations.CreateModel(
            name="ProjectTeamMember",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("role", models.CharField(choices=[("PROJECT_MANAGER", "Project Manager"), ("ENGINEER", "Engineer"), ("SUPERVISOR", "Supervisor"), ("ACCOUNTANT", "Accountant"), ("WORKER", "Worker"), ("OTHER", "Other")], default="OTHER", max_length=30)),
                ("is_active", models.BooleanField(default=True)),
                ("assigned_at", models.DateTimeField(auto_now_add=True)),
                ("notes", models.TextField(blank=True)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="team_members", to="projects.project")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="project_assignments", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-assigned_at"]},
        ),
        migrations.AddConstraint(
            model_name="projectteammember",
            constraint=models.UniqueConstraint(fields=("project", "user"), name="unique_project_team_member"),
        ),
    ]
