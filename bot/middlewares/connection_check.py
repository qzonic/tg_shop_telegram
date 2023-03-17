from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from bot.data import exceptions
from bot.handlers import messages
from bot.data.querysets import CustomerQuery


class ConnectionCheckMiddleware(BaseMiddleware):

    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:

        try:
            CustomerQuery.objects.connection_test()
            return await handler(event, data)
        except exceptions.BadConnectionToServer:
            return await data['bot'].send_message(
                event.from_user.id,
                messages.PLEASE_TRY_AGAIN_LATER
            )
