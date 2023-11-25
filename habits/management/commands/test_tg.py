import os

import dotenv
from django.core.management import BaseCommand

from habits.services import telegram_bot

dotenv.load_dotenv()

user_id = os.getenv('CHAT_ID')
message = 'correct'


class Command(BaseCommand):

    def handle(self, *args, **options):
        telegram_bot(user_id, message)
