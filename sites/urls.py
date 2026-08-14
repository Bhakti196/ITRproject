from django.urls import path
from .views import SiteListCreateView

urlpatterns = [
    path("", SiteListCreateView.as_view(), name="site-list-create"),
]