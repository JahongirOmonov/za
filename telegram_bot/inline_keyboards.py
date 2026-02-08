# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# inline_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='HA', callback_data='HA'),
#             InlineKeyboardButton(text='YOQ', callback_data='yoq')
#         ]
#     ]
# )


from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_builder = InlineKeyboardBuilder()
for i in range(1,101):
    inline_builder.button(text=f'{i}', callback_data=f'{i}')
inline_builder.adjust(1,2,3,2,1, repeat=True)

inline_builder = inline_builder.as_markup()