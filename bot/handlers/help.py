from aiogram import types
from aiogram.filters import CommandObject

from bot.handlers import messages
from bot.handlers.bot_commands import bot_commands


async def help_command(message: types.Message, command: CommandObject):
    print(command.args)
    if command.args:
        if command.args in bot_commands:
            return await message.answer(
                messages.COMMAND_INFO.format(
                    command.args,
                    bot_commands[command.args][0],
                    bot_commands[command.args][1]
                )
            )
        else:
            return await message.answer('Команда не найдена')
    return await message.answer(messages.HELP_COMMAND)
