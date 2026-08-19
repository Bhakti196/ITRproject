from django.urls import path
from .views import labour, labour_detail

urlpatterns = [
    path("", labour, name="labour"),
    path("<int:pk>/", labour_detail, name="labour_detail"),
]