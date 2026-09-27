from django.contrib import admin
from .models import Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "project",
        "pay_period_start",
        "pay_period_end",
        "net_pay",
        "payment_status",
    )
    list_filter = ("payment_status", "project")
    search_fields = ("employee__full_name", "employee__username")