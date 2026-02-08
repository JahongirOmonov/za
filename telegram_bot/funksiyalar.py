from aiogram.types import Message
from aiogram import Bot
import inline_keyboards
import outline_keyboards


async def bot_ishga_tushganda(bot: Bot):
    await bot.send_message(text="Bot ishga tushdi...", chat_id=8071661785)


async def bot_ishdan_toxtaganda(bot: Bot):
    await bot.send_message(text="Bot ishdan to'xtadi...", chat_id=8071661785)


async def start_bosganda(message: Message):
    await message.answer("Choose some of them", reply_to_message_id=message.message_id, reply_markup=inline_keyboards.inline_builder)

