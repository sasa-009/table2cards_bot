from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from utils.states import Search
from search.functions import *

search_r = Router()

@search_r.message(Command('search'))
async def cmd_start_search(message: Message, state: FSMContext):
    await start_search_func(message, state)

@search_r.callback_query(F.data == 'search')
async def start_search(callback: CallbackQuery, state: FSMContext):
    await start_search_func(callback, state)


@search_r.message(Search.word)
async def search(message: Message, state: FSMContext):
    await search_func(message, state)


@search_r.callback_query(F.data == 'edit')
async def edit(callback: CallbackQuery, state: FSMContext):
    await edit_func(callback, state)

@search_r.message(Search.edit)
async def get_edit(message: Message, state: FSMContext):
    await get_edit_func(message, state)

@search_r.callback_query(F.data == 'delete')
async def delete(callback: CallbackQuery, state: FSMContext):
    await delete_func(callback, state)