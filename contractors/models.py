from django.db import models
from accounts.models import CustomUser
from sites.models import Site


class Contractor(models.Model):

    contractor_name = models.CharField(max_length=200)

    company_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    email = models.EmailField(blank=True)

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name="contractors"
    )

    contract_value = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.contractor_name