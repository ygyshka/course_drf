import os

import dotenv
import requests


def telegram_bot(chat_id, message):

    dotenv.load_dotenv()
    bot_api_key = os.getenv('BOT_API_KEY')
    params = {'chat_id': chat_id, 'message': message}
    requests.post(f'https://api.telegram.org/bot{bot_api_key}/sendMessage', params=params)
