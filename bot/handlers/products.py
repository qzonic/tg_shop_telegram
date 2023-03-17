from aiogram.types import CallbackQuery

from bot.data import exceptions
from bot.handlers import messages
from bot.data.querysets import ProductQuery
from bot.keyboards import products_keyboard
from bot.handlers.callback_data_states import (
    LessonCallBackData,
    ProductCallBackData,
)


async def all_products(call: CallbackQuery, callback_data: LessonCallBackData):
    try:
        products = ProductQuery.objects.all(callback_data.slug)
        keyboard = products_keyboard.products_keyboard(products, many=True)
        await call.message.edit_text(
            'Доступные товары',
            reply_markup=keyboard
        )

    except exceptions.BadConnectionToServer:
        await call.message.answer(messages.PLEASE_TRY_AGAIN_LATER)


async def product_detail(call: CallbackQuery, callback_data: ProductCallBackData):
    try:
        product = ProductQuery.objects.get(callback_data.lesson, callback_data.slug)
        keyboard = products_keyboard.products_keyboard(product)
        await call.message.edit_text(
            text=messages.PRODUCT_INFO.format(
                product.title,
                product.price
            ),
            reply_markup=keyboard
        )
    except exceptions.BadConnectionToServer:
        await call.message.answer(messages.PLEASE_TRY_AGAIN_LATER)
