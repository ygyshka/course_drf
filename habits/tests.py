from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from habits.models import Habit
from users.models import User


# Create your tests here.

class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@mail.ru',
            is_staff=False,
            is_superuser=True,
        )
        self.user.set_password('test')
        self.user.save()
        self.access_token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.habit = Habit(
            action='run',
            time='18:00',
            place='outdoor',
            periodicity=3,
            is_publish=True,
            time_to_do=18,
            user=self.user
        )
        self.habit.save()

    def test_habit_create(self):
        """ Текстирование создания привычки """

        data = {
            'action': self.habit.action,
            'place': self.habit.place,
            'time': self.habit.time,
            'user': self.habit.user.id,
            'periodicity': self.habit.periodicity,
            'time_to_do': self.habit.time_to_do
        }
        response = self.client.post('/habit/create', data=data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_habit_delete(self):
        """ Тестирование удаления привычки """

        response = self.client.delete(f'/habit/delete/{self.habit.id}')
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_habit_update(self):
        """ Тестирование обновления привычки """

        data = {
            'time_to_do': 75,
            'place': 'another place'
        }
        response = self.client.patch(f'/habit/update/{self.habit.id}', data=data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['time_to_do'], data['time_to_do']
        )
        self.assertEqual(
            response.data['place'], data['place']
        )

    def test_habit_list(self):
        """ Тестирование получения списка привычек """

        response = self.client.get(f'/habits/list')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habit_retrieve(self):
        """ Тестирование получения отдельной привычки """
        response = self.client.get(f'/habit/{self.habit.id}')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['action'], self.habit.action
        )
        self.assertEqual(
            response.data['place'], self.habit.place
        )
