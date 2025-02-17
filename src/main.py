from aiogram import Bot, Dispatcher
from handlers.startCommandHander import start_command_router
from dotenv import load_dotenv
import os
import asyncio
from locales.lang import Lang
localizator = Lang('en')
translator = localizator.set_lang()
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(start_command_router)
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())