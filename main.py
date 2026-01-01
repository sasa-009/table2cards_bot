import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import CommandStart

from config import TOKEN
from utils.utils import create_keyboard
from utils.lang import M
from search.handlers import search_r
from tags.handlers import tags_r
from randword.handlers import randword
from settings.handlers import settings_r
from add.handlers import add
from repeat.hendlers import repeat_r
from stats.handlers import stats_r
from loadfile.handlers import loadfile

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = create_keyboard([['load_file', 'settings'],['random_words', 'study'],['stats', 'add_words'], ['search', 'tags']])
    await message.answer(M('start'), reply_markup=keyboard)

async def main():
    dp.include_router(randword)
    dp.include_router(settings_r)
    dp.include_router(add)
    dp.include_router(repeat_r)
    dp.include_router(stats_r)
    dp.include_router(search_r)
    dp.include_router(tags_r)
    dp.include_router(loadfile)    
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('exit')