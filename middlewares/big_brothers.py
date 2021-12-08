from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from app import logger
from config import banned_users


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logger.info("[__________________________Новый апдейт____________________________]")
        logger.info("1. ПреПроцесс Апдейт")
        logger.info("Следующая process Update")
        data["middlewares_data"] = "on_pre_process_message"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        if user in banned_users:
            raise CancelHandler()

    async def on_process_update(self, update: types.Update, data: dict):
        logger.info("2. Process update")
        logger.info("Следующая Pre-process Message")

    async def on_pre_process_message(self, message: types.Message, data: dict):
        logger.info("3. Pre-Process Message")
        logger.info("Следующая Filters")
        data["middlewares_data"] = "Process Message"


