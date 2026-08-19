from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Labour
from .serializers import LabourSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def labour(request):

    if request.method == "GET":
        records = Labour.objects.all().order_by("-created_at")
        serializer = LabourSerializer(records, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = LabourSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def labour_detail(request, pk):

    try:
        labour_record = Labour.objects.get(pk=pk)
    except Labour.DoesNotExist:
        return Response(
            {"detail": "Labour record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    labour_record.delete()

    return Response(
        {"detail": "Labour record deleted successfully."},
        status=status.HTTP_204_NO_CONTENT
    )