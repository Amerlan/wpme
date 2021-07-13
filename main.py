from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor
import re
import os


load_dotenv()

API_TOKEN = os.getenv('TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text='Отправь мне номер если не хочешь сохранять его в WhatsApp. Я дам тебе ссылку на WhatsApp'
    )


@dp.message_handler()
async def test(msg: types.Message):
    await bot.send_message(chat_id=msg.chat.id, text=msg.text)
    number = re.fullmatch(pattern='^+\d', string=msg.text)


if '__main__' == __name__:
    executor.start_polling(dispatcher=dp, reset_webhook=False)
