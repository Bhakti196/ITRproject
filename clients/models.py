from django.conf import settings
from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_clients'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name