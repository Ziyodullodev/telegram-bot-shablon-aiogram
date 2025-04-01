from aiogram import types
from aiogram.filters import CommandStart
from handlers.mainHandler import localizator
from aiogram import Router

message_router = Router()

@message_router.message(CommandStart())
async def start_dispatcher(message: types.Message):
    first_name = message.from_user.first_name
    chat_id = message.chat.id
    localizator.set_language("en")
    await message.answer(localizator.get("welcome"))
