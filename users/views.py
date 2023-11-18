from django.shortcuts import render
from rest_framework import generics

from users.serializer import UserRegisterSerializer


# Create your views here.

class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    pass

