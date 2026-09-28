from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL), ("projects", "0002_Project_budget")]
    operations = [
        migrations.CreateModel(
            name="Estimate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("estimate_number", models.CharField(max_length=100, unique=True)),
                ("title", models.CharField(max_length=200)),
                ("status", models.CharField(choices=[("DRAFT", "Draft"), ("SUBMITTED", "Submitted"), ("APPROVED", "Approved"), ("REJECTED", "Rejected")], default="DRAFT", max_length=20)),
                ("notes", models.TextField(blank=True)), ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="created_estimates", to=settings.AUTH_USER_MODEL)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="estimates", to="projects.project")),
            ],
        ),
        migrations.CreateModel(
            name="BOQItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("item_code", models.CharField(blank=True, max_length=50)), ("description", models.CharField(max_length=300)),
                ("unit", models.CharField(max_length=30)), ("quantity", models.DecimalField(decimal_places=3, max_digits=12)),
                ("unit_rate", models.DecimalField(decimal_places=2, max_digits=14)), ("amount", models.DecimalField(decimal_places=2, editable=False, max_digits=16)),
                ("estimate", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="estimates.estimate")),
            ],
        ),
    ]
