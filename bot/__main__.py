import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

import config
from handlers import register_user_commands
from handlers.bot_commands import bot_commands


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands.keys():
        commands_for_bot.append(BotCommand(
            command=cmd,
            description=bot_commands[cmd][0]
        ))

    dp = Dispatcher()
    bot = Bot(token=config.TELEGRAM_TOKEN)
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
