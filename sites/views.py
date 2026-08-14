from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Site
from .serializers import SiteSerializer


class SiteListCreateView(generics.ListCreateAPIView):
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Site.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)