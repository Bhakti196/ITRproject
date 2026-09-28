from decimal import Decimal
from django.db import models
from accounts.models import CustomUser
from projects.models import Project

class Estimate(models.Model):
    STATUS_CHOICES = [("DRAFT", "Draft"), ("SUBMITTED", "Submitted"), ("APPROVED", "Approved"), ("REJECTED", "Rejected")]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="estimates")
    estimate_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_estimates")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
        return sum((item.amount for item in self.items.all()), Decimal("0"))

    def __str__(self):
        return self.estimate_number

class BOQItem(models.Model):
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE, related_name="items")
    item_code = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=300)
    unit = models.CharField(max_length=30)
    quantity = models.DecimalField(max_digits=12, decimal_places=3)
    unit_rate = models.DecimalField(max_digits=14, decimal_places=2)
    amount = models.DecimalField(max_digits=16, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.amount = (self.quantity or Decimal("0")) * (self.unit_rate or Decimal("0"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
