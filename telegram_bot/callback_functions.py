from aiogram.types import CallbackQuery

async def pressed_HA(callback: CallbackQuery):
    await callback.answer("Xabar o'chirildi", cache_time=30)
    await callback.message.delete()
