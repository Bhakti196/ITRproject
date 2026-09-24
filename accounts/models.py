from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('ENGINEER', 'Site Engineer'),
        ('SUPERVISOR', 'Supervisor'),
        ('ACCOUNTANT', 'Accountant'),
    ]

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='ENGINEER'
    )

    def __str__(self):
        return self.username