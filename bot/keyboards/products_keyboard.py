from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.handlers.callback_data_states import (
    ProductCallBackData,
    LessonCallBackData,
    BackCallBackData
)


def products_keyboard(products, many=False):
    keyboard = InlineKeyboardBuilder()
    if not many:
        keyboard.button(
            text='Купить',
            callback_data=ProductCallBackData(
                slug=products.slug,
                lesson=products.lesson
            )
        )
        keyboard.button(
            text='Назад',
            callback_data=LessonCallBackData(
                slug=products.lesson
            )
        )
    else:
        for product in products:
            keyboard.button(
                text=product.title,
                callback_data=ProductCallBackData(
                    slug=product.slug,
                    lesson=product.lesson
                )
            )
        keyboard.button(
            text='Назад',
            callback_data=BackCallBackData()
        )
    keyboard.adjust(1, 1)
    return keyboard.as_markup()
