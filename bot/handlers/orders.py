from aiogram.types import Message

from bot.data import exceptions
from bot.data.querysets import OrderQuery
from bot.handlers import messages
from bot.keyboards.orders_keyboard import orders_keyboard


async def all_orders(message: Message):
    try:
        orders = OrderQuery.objects.all(message.from_user.id)
        keyboard = orders_keyboard(orders)
        await message.answer('Покупки', reply_markup=keyboard)
    except exceptions.BadConnectionToServer:
        await message.answer(messages.PLEASE_TRY_AGAIN_LATER)
