from aiogram import Router
from aiogram import types
from aiogram.filters import CommandStart
start_command_router = Router()
from main import localizator, translator as _

@start_command_router.message(CommandStart())
async def start_dispatcher(message: types.Message):
    first_name = message.from_user.first_name
    chat_id = message.chat.id
    localizator.lang = 'uz'
    await message.answer(_['welcome'])
        