import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command('help'), state='*')
async def command_help(message: types.Message):
    try:
        logging.info(f'{message.from_user.id} {message.text}')

        await message.answer(f"Привет, {message.from_user.full_name}!\n\n"
                             f"Телеграм бот поможет тебе узнать:\n"
                             f"1. Топ самых дешёвых отелей в городе (команда /lowprice)\n"
                             f"2. Узнать топ самых дорогих отелей в городе (команда /highprice)\n"
                             f"3. Узнать топ отелей, наиболее подходящих по цене и расположению от центра (самые дешёвые и находятся ближе всего к центру) (команда /bestdeal)\n"
                             f"4. Узнать историю поиска отелей (команда /history)")
    except Exception as e:
        logging.exception(e)


# if __name__ == '__main__':
#     executor.start_polling(dp)
