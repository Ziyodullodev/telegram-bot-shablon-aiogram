from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from locales.localizator import Localizator


def admin_menu_keyboard(localizator: Localizator):
    
    keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
    
    buttons = [
        ReplyKeyboardButton(text=localizator.get("keyboard_menu_1")),
    ]
    keyboard.keyboard.append(buttons)
    
    return keyboard
