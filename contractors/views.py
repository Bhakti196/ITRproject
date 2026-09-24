from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Contractor
from .serializers import ContractorSerializer


class ContractorListCreateView(generics.ListCreateAPIView):

    serializer_class = ContractorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contractor.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)