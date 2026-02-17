import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder, Redis
from aiogram_dialog import setup_dialogs

from aio_dialogs.dialogs import user_dialog, admin_dialog
from config.config import BOT_TOKEN, logger, REDIS_HOST, REDIS_PORT, REDIS_DB
from config.main_menu import set_main_menu
from handlers import default_handler, other_handler, error


async def main():
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

    # Инициализируем Redis
    redis = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    # Инициализируем хранилище
    storage = RedisStorage(redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    dp = Dispatcher(storage=storage)


    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(default_handler.router)
    dp.include_router(other_handler.router)
    dp.include_router(error.router)
    dp.include_routers(user_dialog)
    dp.include_routers(admin_dialog)

    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())