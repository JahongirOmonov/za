from asyncio import run
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
import callback_functions

import funksiyalar
from telegram_bot.funksiyalar import bot_ishdan_toxtaganda

TOKEN = "8074064365:AAE4ZHwXvdbzVJ3btW7QjFRxNaAkY2fnUU4"
dp = Dispatcher()

async def main():

    dp.startup.register(funksiyalar.bot_ishga_tushganda)
    dp.message.register(funksiyalar.start_bosganda, CommandStart)
    dp.callback_query.register(callback_functions.pressed_HA, F.data.lower()=='ha')
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.shutdown.register(bot_ishdan_toxtaganda)
    await dp.start_polling(bot)

run(main())
