from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Labour
from .serializers import LabourSerializer


class LabourListCreateView(generics.ListCreateAPIView):

    serializer_class = LabourSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Labour.objects.filter(
            created_by=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
        )


class LabourDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = LabourSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Labour.objects.filter(
            created_by=self.request.user
        )