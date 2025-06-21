from aiogram import types
from handlers.mainHandler import localizator, db
from aiogram import Router

message_router = Router()

@message_router.message()
async def message_handler(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    
    await message.answer(text)

