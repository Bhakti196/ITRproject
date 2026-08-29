from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Material
from .serializers import MaterialSerializer


class MaterialListCreateView(generics.ListCreateAPIView):

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Material.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def material_detail(request, pk):

    try:
        material = Material.objects.get(
            pk=pk,
            created_by=request.user
        )

    except Material.DoesNotExist:
        return Response(
            {"detail": "Material record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    material.delete()

    return Response(
        {"detail": "Material record deleted successfully."},
        status=status.HTTP_204_NO_CONTENT
    )