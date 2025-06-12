from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from app.serializers import TaskSerializers , UserSerializers
from app.models import Task , User

# Create your views here.




class TaskCreateSerializers(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.objects.filter(user = self.request.user)

    def perform_create(self , serializer):
        return serializer.save(user = self.request.user)


class TaskDetailSerializers(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user) 

class UserCreateSerializers(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserDetailSerializers(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers





class RegisterView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=201)

from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    pass
