from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from locales.localizator import Localizator

def main_menu_keyboard(localizator: Localizator):
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    
    buttons = [
        InlineKeyboardButton(text=localizator.get("keyboard_menu_1"), callback_data="welcome"),
    ]
    keyboard.inline_keyboard.append(buttons)
    
    return keyboard