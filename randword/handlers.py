from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters.command import Command

from randword.functions import *


randword = Router()


@randword.message(Command('random_words'))
async def random_words_cmd(message: Message):
    await random_words_func(message)

@randword.callback_query(F.data == 'random_words')
async def random_words(callback: CallbackQuery):
    await random_words_func(callback)



@randword.callback_query(F.data.startswith('yes_'))
async def yes(callback: CallbackQuery):
    await yes_func(callback)
        

@randword.callback_query(F.data.startswith('no_'))
async def no(callback: CallbackQuery):
    await no_func(callback)