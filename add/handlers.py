from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command


from add.functions import *

add = Router()


class Words(StatesGroup):
    mes_words = State()

@add.message(Command("add_words"))
async def cmd_add_words(message: Message, state: FSMContext):
    await add_words_func(message, state)
    

@add.callback_query(F.data == 'add_words')
async def add_words(callback: CallbackQuery, state: FSMContext):
    await add_words_func(callback, state)

@add.message(Words.mes_words)
async def get_word(message: Message, state: FSMContext):
    await get_word_func(message, state)


    