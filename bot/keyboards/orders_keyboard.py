from aiogram.utils.keyboard import InlineKeyboardBuilder


def orders_keyboard(orders):
    keyboard = InlineKeyboardBuilder()
    for order in orders:
        keyboard.button(
            text=order.product.title,
            url=order.product.link
        )
    keyboard.adjust(1, 1)
    return keyboard.as_markup()
