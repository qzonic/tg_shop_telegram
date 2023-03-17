from aiogram.filters.callback_data import CallbackData


class LessonCallBackData(CallbackData, prefix='lesson'):
    slug: str


class ProductCallBackData(CallbackData, prefix='product', sep='/?'):
    slug: str
    lesson: str


class BackCallBackData(CallbackData, prefix='back'):
    pass
