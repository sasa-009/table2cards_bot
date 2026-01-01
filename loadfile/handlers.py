from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters.command import Command

from loadfile.functions import *

loadfile = Router()


@loadfile.message(Command('load_file'))
async def cmd_load_file(message: Message):
    await load_file_func(message)

@loadfile.callback_query(F.data == 'load_file')
async def load_file(callback: CallbackQuery):
    await load_file_func(callback)

@loadfile.message(F.document)
async def handle_document(message: Message):
    await handle_document_func(message)

