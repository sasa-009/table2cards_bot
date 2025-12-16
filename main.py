import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import rm
from repeat import rr


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(rm)
    dp.include_router(rr)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())