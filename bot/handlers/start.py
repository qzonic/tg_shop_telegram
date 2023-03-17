import status
from aiogram import types
from aiogram.filters import CommandObject

from . import messages
from bot.data import exceptions
from bot.data.querysets import CustomerQuery
from bot.keyboards.start_keyboard import start_markup


async def start(message: types.Message, command: CommandObject):
    try:
        user = CustomerQuery.objects.get(message.from_user.id)
        if isinstance(user, int) and user == status.HTTP_404_NOT_FOUND:
            CustomerQuery.objects.create(
                tg_id=message.from_user.id,
                username=message.from_user.username
            )
        await message.answer(messages.START_MESSAGE, reply_markup=start_markup())
    except exceptions.BadConnectionToServer:
        return await message.answer(
            messages.PLEASE_TRY_AGAIN_LATER
        )
