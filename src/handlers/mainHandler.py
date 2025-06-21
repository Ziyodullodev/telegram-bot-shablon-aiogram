from aiogram import Dispatcher
from dotenv import load_dotenv
from locales.localizator import Localizator
from functions.DatabaseSqlite3 import SQLiteDatabase as Database
# from functions.Database import Database
import os
load_dotenv()
SQLITE3_NAME = os.getenv('SQLITE3_NAME')

localizator = Localizator()
dp = Dispatcher()
db = Database(db_path=SQLITE3_NAME)

from handlers.startCommandHander import start_message_router
from handlers.callbackHandler import callback_router
from handlers.messageHandler import message_router
from handlers.adminHandler import admin_router

async def mainHandler(bot):
    dp.include_router(start_message_router)
    dp.include_router(message_router)
    dp.include_router(callback_router)
    dp.include_router(admin_router)
    print("Bot started")
    await dp.start_polling(bot)
