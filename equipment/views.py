from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Equipment
from .serializers import EquipmentSerializer


class EquipmentListCreateView(generics.ListCreateAPIView):

    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Equipment.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)