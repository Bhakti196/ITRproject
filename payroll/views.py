from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Payroll
from .serializers import PayrollSerializer


class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all().order_by("-created_at")
    serializer_class = PayrollSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Payroll.objects.all().order_by("-created_at")
        project_id = self.request.query_params.get("project")
        employee_id = self.request.query_params.get("employee")
        status_param = self.request.query_params.get("status")

        if project_id:
            queryset = queryset.filter(project_id=project_id)
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        if status_param:
            queryset = queryset.filter(payment_status=status_param)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
