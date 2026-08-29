from django.urls import path
from .views import equipment, equipment_detail

urlpatterns = [
    path("", equipment, name="equipment"),
    path("<int:pk>/", equipment_detail, name="equipment_detail"),
]