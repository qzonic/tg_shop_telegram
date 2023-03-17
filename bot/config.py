from os import getenv

from dotenv import load_dotenv


load_dotenv()


TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
SITE_TOKEN = getenv('SITE_TOKEN')
PAYMENTS_TOKEN = getenv('PAYMENTS_TOKEN')
HOST = getenv('HOST')
