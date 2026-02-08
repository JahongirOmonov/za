from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder

outline_builders = ReplyKeyboardBuilder()
outline_builders.button(text='1-tugma')
outline_builders.button(text='1-tugma')
outline_builders.button(text='1-tugma')
for i in range(1, 101):
    outline_builders.button(text=f"{i}")

outline_builders.adjust(1,2,3,4,3,2,1,repeat=False)
outline_builders.row(
    KeyboardButton(text='777'),
    KeyboardButton(text='777'),
    KeyboardButton(text='777'),
    KeyboardButton(text='777'),
    KeyboardButton(text='777'),
    KeyboardButton(text='777'),
    width=2
)

outline_builders = outline_builders.as_markup()
outline_builders.resize_keyboard = True



