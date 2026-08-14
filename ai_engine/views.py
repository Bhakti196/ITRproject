from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import (
    project_completion_risk,
    project_cost_overrun_risk,
    material_stock_analysis,
    labour_requirement_prediction,
    delay_prediction,
)


class ProjectRiskView(APIView):

    def get(self, request, project_id):
        try:
            result = project_completion_risk(project_id)
            return Response(result)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class ProjectCostRiskView(APIView):

    def get(self, request, project_id):
        try:
            result = project_cost_overrun_risk(project_id)
            return Response(result)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class MaterialStockView(APIView):

    def get(self, request, project_id):
        try:
            result = material_stock_analysis(project_id)
            return Response(result)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class LabourRequirementView(APIView):

    def get(self, request, project_id):
        try:
            result = labour_requirement_prediction(project_id)
            return Response(result)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class DelayPredictionView(APIView):

    def get(self, request, project_id):
        try:
            result = delay_prediction(project_id)
            return Response(result)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
       