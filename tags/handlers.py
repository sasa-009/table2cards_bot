from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from utils.states import Tags
from tags.functions import *

tags_r = Router()



@tags_r.callback_query(F.data == 'tags')
async def tags(callback: CallbackQuery):
    await tags_func(callback)

@tags_r.message(Command('tags'))
async def cmd_tags(message: Message):
    await tags_func(message)

@tags_r.callback_query(F.data == 'create_tag')
async def create_tag(callback: CallbackQuery, state: FSMContext):
    await create_tag_func(callback, state)

@tags_r.message(Tags.create)
async def create_tag_(message: Message):
    await create_tag__func(message)

@tags_r.callback_query(F.data == 'delete_tag')
async def delete_tag(callback: CallbackQuery, state: FSMContext):
    await delete_tag_func(callback, state)

@tags_r.message(Tags.delete)
async def delete_tag_(message: Message):
    await delete_tag__func(message)


@tags_r.callback_query(F.data == 'tag_list')
async def tag_list(callback: CallbackQuery):
    await tag_list_func(callback)

@tags_r.callback_query(F.data.startswith('tag:'))
async def tag_(callback: CallbackQuery, state: FSMContext):
    await tag__func(callback, state)


@tags_r.callback_query(F.data == 'add_tag_2_words')
async def add_tag_2_words(callback: CallbackQuery, state: FSMContext):
    await add_tag_2_words_func(callback, state)

@tags_r.message(Tags.add)
async def add_tag(message: Message, state: FSMContext):
    await add_tag_func(message, state)