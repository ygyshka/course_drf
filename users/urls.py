from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

from users.apps import UsersConfig
from users.views import UserRegister, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('list/', UserListAPIView.as_view(), name='user-list')

] # дописать настройки сохранения файлов пользователя
