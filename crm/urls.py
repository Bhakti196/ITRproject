"""
URL configuration for crm project.
"""

from django.contrib import admin
from django.urls import include, path
from accounts.views import home


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/project-team/", include("project_team.urls")),
    path("api/incidents/", include("incidents.urls")),
    path("api/estimates/", include("estimates.urls")),
    path("api/project-team/", include("project_team.urls")),
    path("api/incidents/", include("incidents.urls")),
    path("api/estimates/", include("estimates.urls")),

    # Authentication
    path("api/", include("accounts.urls")),

    # Core modules
    path("api/sites/", include("sites.urls")),
    path("api/projects/", include("projects.urls")),
    path("api/tasks/", include("tasks.urls")),
    path("api/dpr/", include("dpr.urls")),
    path("api/materials/", include("materials.urls")),
    path("api/labour/", include("labour.urls")),
    path("api/contractors/", include("contractors.urls")),
    path("api/equipment/", include("equipment.urls")),
    path("api/billing/", include("billing.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/payroll/", include("payroll.urls")),
       
    # Purchase Management
    path("api/purchase/", include("purchase.urls")),

    # AI
    path("api/ai/", include("ai_engine.urls")),
]