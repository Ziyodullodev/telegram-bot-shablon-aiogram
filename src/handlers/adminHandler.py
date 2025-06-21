from aiogram import types
from aiogram import Router
from aiogram.filters import Command

admin_router = Router()

@admin_router.message(Command("admin"))
async def admin_handler(message: types.Message):
    await message.answer("Admin")
