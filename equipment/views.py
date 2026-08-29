from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Equipment


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def equipment(request):

    if request.method == "GET":
        equipment_records = Equipment.objects.all()

        data = []

        for item in equipment_records:
            data.append({
                "id": item.id,
                "equipment_name": item.equipment_name,
                "equipment_type": item.equipment_type,
                "status": item.status,
                "operator_name": item.operator_name,
                "daily_cost": str(item.daily_cost),
                "last_maintenance": item.last_maintenance,
                "created_at": item.created_at,
                "site": item.site_id,
                "created_by": item.created_by_id,
            })

        return Response(data)

    if request.method == "POST":
        equipment_record = Equipment.objects.create(
            equipment_name=request.data.get("equipment_name"),
            equipment_type=request.data.get("equipment_type"),
            site_id=request.data.get("site"),
            status=request.data.get("status"),
            operator_name=request.data.get("operator_name", ""),
            daily_cost=request.data.get("daily_cost"),
            last_maintenance=request.data.get("last_maintenance"),
            created_by=request.user,
        )

        return Response(
            {
                "id": equipment_record.id,
                "equipment_name": equipment_record.equipment_name,
                "equipment_type": equipment_record.equipment_type,
                "status": equipment_record.status,
                "operator_name": equipment_record.operator_name,
                "daily_cost": str(equipment_record.daily_cost),
                "last_maintenance": equipment_record.last_maintenance,
                "created_at": equipment_record.created_at,
                "site": equipment_record.site_id,
                "created_by": equipment_record.created_by_id,
            },
            status=status.HTTP_201_CREATED
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def equipment_detail(request, pk):

    try:
        equipment_record = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return Response(
            {"detail": "Equipment record not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    equipment_record.delete()

    return Response(
        {"detail": "Equipment deleted successfully."},
        status=status.HTTP_204_NO_CONTENT
    )