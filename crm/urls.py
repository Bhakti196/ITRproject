urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    path("api/project-team/", include("project_team.urls")),
    path("api/incidents/", include("incidents.urls")),
    path("api/estimates/", include("estimates.urls")),

    # Authentication
    path("api/", include("accounts.urls")),

    # Core modules
    path("api/sites/", include("sites.urls")),
    path("api/projects/", include("projects.urls")),
    ...
    path("api/payroll/", include("payroll.urls")),

    # Purchase Management
    path("api/purchase/", include("purchase.urls")),
]