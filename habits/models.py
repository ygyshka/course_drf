import datetime

from django.conf import settings
from django.db import models

import constants


# Create your models here.


class Habit(models.Model):

    action = models.CharField(max_length=150, verbose_name='действие')
    time = models.TimeField(verbose_name='время')
    date = models.DateField(auto_now=True, verbose_name='дата создания')
    place = models.CharField(max_length=100, verbose_name='место', **constants.NULLABLE)
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.CASCADE,
                                         verbose_name='связанная привычка', **constants.NULLABLE)
    periodicity = models.IntegerField(verbose_name='переодичность(количество повторений в неделю)')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', **constants.NULLABLE)
    time_to_do = models.PositiveIntegerField(verbose_name='время на выполнение')
    is_publish = models.BooleanField(default=False, verbose_name='признак публичности')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **constants.NULLABLE)

    def __str__(self):
        return f'{self.action} {self.time} {self.place} {self.periodicity} {self.user}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'




