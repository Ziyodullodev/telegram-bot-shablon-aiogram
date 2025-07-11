from aiogram import types
from handlers.mainHandler import localizator, db
from aiogram import Router
from .keyboards import main_keyboard, admin_keyboard

message_router = Router()

@message_router.message()
async def message_handler(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    user = db.get("users", {"telegram_id": chat_id})
    if not user:
        await message.answer(localizator.get("error"))
        return
    if user.get("step") != "admin_panel":
        await message.answer(text, reply_markup=main_keyboard.main_menu_keyboard(localizator))
        return

