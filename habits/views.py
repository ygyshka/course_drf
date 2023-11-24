from rest_framework import generics

from habits.models import Habit
from habits.paginations import NotesPagination
from habits.serializer import HabitSerializer
from users.permissions import IsOwner


# Create your views here.

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('id')
    pagination_class = NotesPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):

    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitPublishListAPIView(generics.ListAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_publish=True)
