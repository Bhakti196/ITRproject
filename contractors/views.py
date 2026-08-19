from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Contractor
from .serializers import ContractorSerializer


class ContractorListCreateView(generics.ListCreateAPIView):

    serializer_class = ContractorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contractor.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def contractor_detail(request, pk):

    try:
        contractor = Contractor.objects.get(
            pk=pk,
            created_by=request.user
        )
    except Contractor.DoesNotExist:
        return Response(
            {"detail": "Contractor record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    contractor.delete()

    return Response(
        {"detail": "Contractor record deleted successfully."},
        status=status.HTTP_204_NO_CONTENT
    )