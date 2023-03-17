__all__ = ['register_user_commands', 'bot_commands', 'messages']

from aiogram import Router, F
from aiogram.filters import Command, CommandStart

from bot.handlers import messages
from bot.handlers.start import start
from bot.handlers.help import help_command
from bot.handlers.lessons import all_lessons
from bot.handlers.products import all_products, product_detail
from bot.handlers.orders import all_orders
from bot.handlers.callback_data_states import (
    LessonCallBackData,
    ProductCallBackData,
    BackCallBackData
)
from bot.middlewares.connection_check import ConnectionCheckMiddleware


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(all_lessons, F.text == messages.LESSONS)
    router.message.register(all_orders, F.text == messages.ORDERS)

    router.callback_query.register(all_products, LessonCallBackData.filter())
    router.callback_query.register(product_detail, ProductCallBackData.filter())
    router.callback_query.register(all_lessons, BackCallBackData.filter())

    router.message.middleware(ConnectionCheckMiddleware())
    router.callback_query.middleware(ConnectionCheckMiddleware())
