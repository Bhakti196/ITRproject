from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Material
from .serializers import MaterialSerializer


class MaterialListCreateView(generics.ListCreateAPIView):

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Material.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)