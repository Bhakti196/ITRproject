from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Incident
from .serializers import IncidentSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(project__created_by=self.request.user).select_related("project", "reported_by")

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status in {"RESOLVED", "CLOSED"} and instance.resolved_at is None:
            instance.resolved_at = timezone.now()
            instance.save(update_fields=["resolved_at"])
