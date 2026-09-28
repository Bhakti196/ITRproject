from django.urls import path
from .views import ContractorListCreateView, ContractorDetailView

urlpatterns = [
    path(
        '',
        ContractorListCreateView.as_view(),
        name='contractor-list-create'
    ),
    path(
        '<int:pk>/',
        ContractorDetailView.as_view(),
        name='contractor-detail'
    ),
]