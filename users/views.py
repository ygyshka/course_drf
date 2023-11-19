from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.serializer import UserRegisterSerializer, UserListSerializer


# Create your views here.

class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserListAPIView(generics.ListAPIView):

    serializer_class = UserListSerializer
    queryset = User.objects.all()
    # permission_classes = [IsStaff, IsAdmin, IsSuperUser]
