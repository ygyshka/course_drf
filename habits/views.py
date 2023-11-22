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
    queryset = Habit.objects.all()
    pagination_class = NotesPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


    # def get_permissions(self):
    #     if not self.queryset.is_publish:
    #         permission_classes = [IsOwner]
    #     else:
    #         permission_classes = [~IsOwner]
    #     return [permission() for permission in permission_classes]


class HabitUpdateAPIView(generics.UpdateAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):

    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
