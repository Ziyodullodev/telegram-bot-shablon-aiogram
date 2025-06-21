from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from .keyboards import admin_keyboard, main_keyboard
from .mainHandler import localizator, db
admin_router = Router()

