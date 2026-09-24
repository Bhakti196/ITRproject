from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Billing
from .serializers import BillingSerializer


class BillingListCreateView(generics.ListCreateAPIView):

    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Billing.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)