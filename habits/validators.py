from rest_framework.exceptions import ValidationError

# from habits.models import Habit


class ValidTimeToDo:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        temp_val = dict(value).get(self.field)
        if int(temp_val) > 120:
            raise ValidationError("Время выполнения привычки не должно превышать 120 секунд")


class ValidPeriod:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        temp_value = dict(value).get(self.field)
        if temp_value is not None and int(temp_value) <= 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")


class ValidAward:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        temp1 = dict(value).get(self.field1)
        temp2 = dict(value).get(self.field2)
        if temp1 and temp2:
            raise ValidationError("Невозможно одновременно указывать связанную привычку и вознаграждние")


class ValidAssociatedHabit:

    def __init__(self):
        pass

    def __call__(self, value):

        if value.get('associated_habit'):
            if not value.get('associated_habit').is_nice:
                raise ValidationError("В связанные привычки могут попадать "
                                      "только привычки с признаком приятной привычки")


class ValidHabitIsNiceAndReward:

    def __init__(self):
        pass

    def __call__(self, value):
        if value.get('is_nice') and value.get('reward') is not None:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")
        elif value.get('is_nice') and value.get('associated_habit') is not None:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")
