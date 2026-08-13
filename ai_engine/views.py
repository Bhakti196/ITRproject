from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import project_completion_risk


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