import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import rm
from repeat import rr
from stats import rs
from add import ra
from search import rsrh


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(rm)
    dp.include_router(rr)
    dp.include_router(rs)
    dp.include_router(ra)
    dp.include_router(rsrh)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("exit")