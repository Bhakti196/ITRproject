from django.db import models
from accounts.models import CustomUser
from billing.models import Billing


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ("CASH", "Cash"),
        ("BANK", "Bank Transfer"),
        ("UPI", "UPI"),
        ("CHEQUE", "Cheque"),
    ]

    bill = models.ForeignKey(
        Billing,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    payment_date = models.DateField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )

    reference_number = models.CharField(
        max_length=100,
        blank=True
    )

    remarks = models.TextField(
        blank=True
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Payment - {self.bill.invoice_number}"