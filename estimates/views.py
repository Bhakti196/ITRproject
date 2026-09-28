from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Estimate, BOQItem
from .serializers import EstimateSerializer, EstimateCreateSerializer, BOQItemSerializer

class EstimateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Estimate.objects.filter(created_by=self.request.user).prefetch_related("items").select_related("project")

    def get_serializer_class(self):
        return EstimateCreateSerializer if self.action in {"create", "update", "partial_update"} else EstimateSerializer

class BOQItemViewSet(viewsets.ModelViewSet):
    serializer_class = BOQItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BOQItem.objects.filter(estimate__created_by=self.request.user).select_related("estimate")
