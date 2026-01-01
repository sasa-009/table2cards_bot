from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters.command import Command

from repeat.functions import *

repeat_r = Router()






@repeat_r.message(Command('study'))
async def cmd_study(message: Message):
    await study_func(message)

@repeat_r.callback_query(F.data == 'study')
async def study(callback: CallbackQuery):
    await study_func(callback)

@repeat_r.callback_query(F.data == 'repeat')
async def repeat(callback: CallbackQuery):
    await repeat_func(callback)


@repeat_r.callback_query(F.data == 'continue')
async def continue_r(callback: CallbackQuery):
    await continue_r_func(callback)


@repeat_r.callback_query(F.data.startswith('r-yes_'))
async def yes_r(callback: CallbackQuery):
    await yes_r_func(callback)


@repeat_r.callback_query(F.data.startswith('r-no_'))
async def no_r(callback: CallbackQuery):
    await no_r_func(callback)
