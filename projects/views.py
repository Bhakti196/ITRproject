from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer


class ProjectListCreateView(generics.ListCreateAPIView):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def project_detail(request, pk):

    try:
        project = Project.objects.get(
            pk=pk,
            created_by=request.user
        )

    except Project.DoesNotExist:
        return Response(
            {"detail": "Project record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    project.delete()

    return Response(
        {"detail": "Project record deleted successfully."},
        status=status.HTTP_204_NO_CONTENT
    )