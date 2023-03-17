from typing import Union

from aiogram import types

from bot.data import exceptions
from bot.handlers import messages
from bot.data.querysets import LessonQuery
from bot.keyboards.lessons_keyboard import lessons_keyboard


async def all_lessons(message: Union[types.Message, types.CallbackQuery]):
    try:
        lessons = LessonQuery.objects.all()
        keyboard = lessons_keyboard(lessons)
        if isinstance(message, types.Message):
            return await message.answer(
                'Доступные предметы',
                reply_markup=keyboard
            )
        return message.message.edit_text(
            'Доступные предметы',
            reply_markup=keyboard
        )
    except exceptions.BadConnectionToServer:
        await message.answer(messages.PLEASE_TRY_AGAIN_LATER)
