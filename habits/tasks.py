import os
from datetime import datetime, timedelta

import dotenv
from celery import shared_task

from habits.models import Habit
from habits.services import telegram_bot
from users.models import User


@shared_task
def send_message_habits():
    now = datetime.now().time()
    if User.objects.all().exists:

        for user in User.objects.all():
            chat_id = user.telegram_chat_id

            for habit in Habit.objects.filter(user=user):
                habit_time = habit.time
                time_diff = (datetime.combine(datetime.today(), habit_time)
                             - datetime.combine(datetime.today(), now))
                if time_diff <= timedelta(minutes=10):
                    telegram_bot(chat_id, message=f'Напоминание: пора выполнить привычку: {habit.action}')
