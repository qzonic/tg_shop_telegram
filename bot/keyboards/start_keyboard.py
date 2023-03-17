from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.handlers import messages


def start_markup():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=messages.LESSONS)
    keyboard.button(text=messages.ORDERS)
    return keyboard.as_markup(resize_keyboard=True)
