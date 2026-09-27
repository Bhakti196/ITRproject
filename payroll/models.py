from django.db import models
from projects.models import Project
from accounts.models import CustomUser


class Payroll(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("HOLD", "On Hold"),
    ]

    PAYMENT_MODE_CHOICES = [
        ("CASH", "Cash"),
        ("BANK_TRANSFER", "Bank Transfer"),
        ("CHEQUE", "Cheque"),
        ("UPI", "UPI"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="payroll_records"
    )

    employee = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="payroll_records"
    )

    pay_period_start = models.DateField()

    pay_period_end = models.DateField()

    basic_pay = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    overtime_hours = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    overtime_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    allowances = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    net_pay = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
        editable=False
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="PENDING"
    )

    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_MODE_CHOICES,
        blank=True
    )

    payment_date = models.DateField(
        null=True,
        blank=True
    )

    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="payroll_created"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        overtime_pay = (self.overtime_hours or 0) * (self.overtime_rate or 0)
        self.net_pay = (
            (self.basic_pay or 0)
            + overtime_pay
            + (self.allowances or 0)
            - (self.deductions or 0)
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} - {self.pay_period_start} to {self.pay_period_end}"
