from rest_framework import serializers

from habits.models import Habit
from habits.validators import ValidTimeToDo, ValidPeriod, ValidAward, ValidAssociatedHabit, ValidHabitIsNiceAndReward


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            ValidTimeToDo(field='time_to_do'),
            ValidPeriod(field='periodicity'),
            ValidAward(field1='associated_habit', field2='reward'),
            ValidAssociatedHabit(),
            ValidHabitIsNiceAndReward(),
            ]
