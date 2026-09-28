from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Payment
from .serializers import PaymentSerializer


class PaymentListCreateView(generics.ListCreateAPIView):

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def payment_detail(request, pk):

    try:
        payment = Payment.objects.get(
            pk=pk,
            created_by=request.user
        )
    except Payment.DoesNotExist:
        return Response(
            {"detail": "Payment record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    payment.delete()

    return Response(
        {"detail": "Payment record deleted successfully."},
        status=status.HTTP_204_NO_CONTENT
    )