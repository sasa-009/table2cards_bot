import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.handlers import rm
from handlers.repeat import rr
from handlers.stats import rs
from handlers.add import ra
from handlers.search import rsrh
from handlers.tags import rt


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(rm)
    dp.include_router(rr)
    dp.include_router(rs)
    dp.include_router(ra)
    dp.include_router(rsrh)
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("exit")