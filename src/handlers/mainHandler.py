from aiogram import Dispatcher
from locales.localizator import Localizator

localizator = Localizator()
dp = Dispatcher()
from handlers.startCommandHander import message_router

async def mainHandler(bot):
    dp.include_router(message_router)
    print("Bot started")
    await dp.start_polling(bot)
