from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from app.serializers import TaskSerializers , PeopleSerializers
from app.models import Task , People
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()



class TaskCreateSerializers(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


class TaskDetailSerializers(RetrieveUpdateDestroyAPIView):

    # queryset = Task.objects.all()
    serializer_class = TaskSerializers
    
    # def get(self , request):
    #     people = self.get_object()
    #     print(people)
    def get_queryset(self ):
        print(self.request.user)
        # return Task.objects.filter(task_people = self.request.user['id'])
        # return Task.objects.filter(task_poeple = 4)

class PeopleCreateSerializers(ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers

class PeopleDetailSerializers(RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers


from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    pass
