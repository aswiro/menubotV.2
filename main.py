import os

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv("MENU_TOKEN")

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)

storage = RedisStorage2('localhost', 6379)
dp = Dispatcher(bot, storage=storage)
