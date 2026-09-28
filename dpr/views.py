from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import DailyProgressReport
from .serializers import DailyProgressReportSerializer


class DPRListCreateView(generics.ListCreateAPIView):
    serializer_class = DailyProgressReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DailyProgressReport.objects.filter(
            created_by=self.request.user
        ).order_by("-report_date", "-created_at")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DPRDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DailyProgressReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DailyProgressReport.objects.filter(
            created_by=self.request.user
        )