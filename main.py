from aiogram import executor
import logging
from botrequests import *
import errors
from loader import dp, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    # Создаем таблицы в БД
    try:
        db.create_table_users()
        db.create_table_history()
    except Exception as e:
        logging.exception('Ну ё маё!')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
