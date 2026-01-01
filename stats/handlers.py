from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters.command import Command

from stats.functions import *

stats_r = Router()


@stats_r.message(Command('stats'))
async def stats(message: Message):
    await stats_func(message)

@stats_r.callback_query(F.data == 'stats')
async def stats(callback: CallbackQuery):
    await stats_func(callback)


@stats_r.callback_query(F.data == 'known')
async def known(callback: CallbackQuery):
    await known_func(callback)


@stats_r.callback_query(F.data == 'unknown')
async def unknown(callback: CallbackQuery):
    await unknown_func(callback)