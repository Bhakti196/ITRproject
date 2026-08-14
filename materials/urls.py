from django.urls import path
from .views import MaterialListCreateView

urlpatterns = [
    path("", MaterialListCreateView.as_view(), name="materials"),
]