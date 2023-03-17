from aiogram.utils.keyboard import (
    InlineKeyboardBuilder
)

from bot.handlers.callback_data_states import LessonCallBackData


def lessons_keyboard(lessons):
    keyboard = InlineKeyboardBuilder()
    for lesson in lessons:
        keyboard.button(
            text=lesson.title,
            callback_data=LessonCallBackData(
                slug=lesson.slug
            )
        )
    keyboard.adjust(1, 1)
    return keyboard.as_markup()
