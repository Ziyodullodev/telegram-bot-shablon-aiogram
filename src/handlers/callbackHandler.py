from aiogram import types
from .keyboards import admin_keyboard, main_keyboard
from .mainHandler import localizator
from aiogram import Router

callback_router = Router()

@callback_router.callback_query(lambda c: c.data == "welcome")
async def check_channel(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(localizator.get("welcome"), reply_markup=main_keyboard.main_menu_keyboard(localizator))
    return
    
    
