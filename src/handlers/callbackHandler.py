from aiogram import types
from .keyboards import admin_keyboard, main_keyboard
from .mainHandler import localizator
from aiogram import Router

callback_router = Router()

@callback_router.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(localizator.get("welcome"))
