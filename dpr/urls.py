from django.urls import path
from .views import DPRListCreateView

urlpatterns = [
    path("", DPRListCreateView.as_view(), name="dpr"),
]