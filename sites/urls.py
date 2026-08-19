from django.urls import path

from .views import SiteListCreateView, site_detail


urlpatterns = [
    path(
        "",
        SiteListCreateView.as_view(),
        name="sites",
    ),

    path(
        "<int:pk>/",
        site_detail,
        name="site_detail",
    ),
]