import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command('history'), state='*')
async def command_help(message: types.Message):
    pass
