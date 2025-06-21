from aiogram import types
from aiogram.filters import CommandStart, Command
from handlers.mainHandler import localizator, db
from aiogram import Router
from .keyboards import main_keyboard, admin_keyboard

start_message_router = Router()

@start_message_router.message(CommandStart())
async def start_dispatcher(message: types.Message):
    first_name = message.from_user.first_name
    chat_id = message.chat.id
    
    user = db.get("users", {"telegram_id": chat_id})
    if not user:
        language = message.from_user.language_code or "uz"
        if language not in ["uz", "ru", "en"]:
            language = "uz"
        db.insert("users", {
            "telegram_id": chat_id,
            "username": message.from_user.username if message.from_user.username else chat_id,
            "first_name": first_name if first_name else "user " + str(chat_id),
            "last_name": message.from_user.last_name if message.from_user.last_name else "",
            "phone_number": "",
            "step": "start",
            "language": language
        })
    else:
        language = user.get("language", "uz")
    
    localizator.set_language(language)
    await message.answer(localizator.get("welcome"), reply_markup=main_keyboard.main_menu_keyboard(localizator))


@start_message_router.message(Command("panel"))
async def admin_handler(message: types.Message):
    user = db.get("users", {"telegram_id": message.chat.id})
    
    if not user or not user.get("is_admin"):
        await message.answer("You are not an admin")
        return
    db.update("users", {"step": "admin_panel"}, {"telegram_id": message.chat.id})
    await message.answer("Admin panel", reply_markup=admin_keyboard.admin_menu_keyboard(localizator))


@start_message_router.message(Command("exit"))
async def exit_handler(message: types.Message):
    user = db.get("users", {"telegram_id": message.chat.id})
    
    if not user or not user.get("is_admin"):
        await message.answer("You are not an admin")
        return
    db.update("users", {"step": "start"}, {"telegram_id": message.chat.id})
    await message.answer("You have been logged out", reply_markup=main_keyboard.main_menu_keyboard(localizator))

