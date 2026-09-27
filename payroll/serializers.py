from rest_framework import serializers
from .models import Payroll


class PayrollSerializer(serializers.ModelSerializer):

    employee_name = serializers.CharField(source="employee.full_name", read_only=True)
    project_name = serializers.CharField(source="project.project_name", read_only=True)
    overtime_pay = serializers.SerializerMethodField()

    class Meta:
        model = Payroll
        fields = [
            "id",
            "project",
            "project_name",
            "employee",
            "employee_name",
            "pay_period_start",
            "pay_period_end",
            "basic_pay",
            "overtime_hours",
            "overtime_rate",
            "overtime_pay",
            "allowances",
            "deductions",
            "net_pay",
            "payment_status",
            "payment_mode",
            "payment_date",
            "notes",
            "created_by",
            "created_at",
        ]
        read_only_fields = ["net_pay", "created_by", "created_at"]

    def get_overtime_pay(self, obj):
        return (obj.overtime_hours or 0) * (obj.overtime_rate or 0)
