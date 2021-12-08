from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram import executor
from utils.logging_controllers import logger
# import middlewares, filters, handlers

from main import dp, bot

dp.middleware.setup(LoggingMiddleware(logger))


async def on_startup(dispatcher):
    pass
    # await bot.set_webhook(config.WEBHOOK_URL)
    # await start.register_start_handlers(dp)   # insert code here to run it after start


async def on_shutdown(dispatcher):
    logger.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()
    # db._conn.close()

    logger.warning('Bye!')


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        # webhook_path=config.WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        # host=config.WEBAPP_HOST,
        # port=config.WEBAPP_PORT,
    )
