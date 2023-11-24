from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitDestroyAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitRetrieveAPIView, HabitPublishListAPIView

app_name = HabitsConfig.name

urlpatterns = [

    path('habits/', HabitListAPIView.as_view(), name='habits-list'),
    path('habits/list', HabitPublishListAPIView.as_view(), name='habits-publish-list'),
    path('habit/create', HabitCreateAPIView.as_view(), name='habits-create'),
    path('habit/<int:pk>', HabitRetrieveAPIView.as_view(), name='habits-get'),
    path('habit/update/<int:pk>', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('habit/delete/<int:pk>', HabitDestroyAPIView.as_view(), name='habits-delete'),

]
