from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL), ("projects", "0002_Project_budget")]
    operations = [migrations.CreateModel(
        name="Incident",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("incident_date", models.DateField()), ("title", models.CharField(max_length=200)), ("description", models.TextField()),
            ("location", models.CharField(blank=True, max_length=300)),
            ("severity", models.CharField(choices=[("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High"), ("CRITICAL", "Critical")], default="MEDIUM", max_length=20)),
            ("status", models.CharField(choices=[("OPEN", "Open"), ("INVESTIGATING", "Investigating"), ("RESOLVED", "Resolved"), ("CLOSED", "Closed")], default="OPEN", max_length=20)),
            ("corrective_action", models.TextField(blank=True)), ("resolved_at", models.DateTimeField(blank=True, null=True)), ("created_at", models.DateTimeField(auto_now_add=True)),
            ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="incidents", to="projects.project")),
            ("reported_by", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="reported_incidents", to=settings.AUTH_USER_MODEL)),
        ], options={"ordering": ["-incident_date", "-created_at"]},
    )]
