from django.http import HttpResponse

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import RegisterSerializer, UserProfileSerializer


def home(request):
    return HttpResponse("🚀 Construction CRM Backend Running!")


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class EmployeeListView(generics.ListAPIView):
    """Lightweight list of users, used to populate employee pickers
    (e.g. the Payroll 'employee' dropdown) in the frontend."""
    queryset = CustomUser.objects.all().order_by("full_name")
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]