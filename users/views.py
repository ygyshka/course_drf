from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializer import UserRegisterSerializer, UserListSerializer


# Create your views here.

class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [~IsAuthenticated]


class UserListAPIView(generics.ListAPIView):

    serializer_class = UserListSerializer
    queryset = User.objects.all()
