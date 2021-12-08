from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


async def start(msg: types.Message):
    await msg.answer("Привет")


async def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart())
