from aiogram import Bot
from handlers.mainHandler import mainHandler as mainhand
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


async def main():
    bot = Bot(token=BOT_TOKEN)
    await mainhand(bot)

if __name__ == "__main__":
    asyncio.run(main())