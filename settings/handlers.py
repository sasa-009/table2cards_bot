from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters.command import Command, CommandObject

from settings.functions import *
settings_r = Router()

@settings_r.callback_query(F.data == 'settings')
async def settings(callback: CallbackQuery):
    await settings_func(callback)


@settings_r.message(Command('settings'))
async def cmd_settings(message: Message):
    await settings_func(message)


@settings_r.message(Command('transc'))
async def cmd_transc(message: Message, command: CommandObject):
    await cmd_transc_func(message, command)


@settings_r.message(Command('quantity'))
async def cmd_quantity(message: Message, command: CommandObject):
    await cmd_quantity_func(message, command)


@settings_r.message(Command('lang'))
async def cmd_lang(message: Message, command: CommandObject):
    await cmd_lang_func(message, command)