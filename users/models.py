from django.contrib.auth.models import AbstractUser
from django.db import models

import constants


# Create your models here.


class User(AbstractUser):

    username = None

    phone = models.CharField(max_length=35, verbose_name='телефон', **constants.NULLABLE)
    email = models.EmailField(unique=True ,verbose_name='почта')
    country = models.CharField(max_length=150, verbose_name='страна', **constants.NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **constants.NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
