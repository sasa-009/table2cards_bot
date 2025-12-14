import asyncio
import logging
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart, Command, CommandObject

from convert import convert
from data import get_data, update_data
from utils import print_word, choose_words, change_data, keybord_words, word_list
from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

i = 1
c = 0
data = get_data()
config = data['config']

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard  = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="load_file", callback_data="load_file"),
            types.InlineKeyboardButton(text="settings", callback_data="settings")
        ],
        [
            types.InlineKeyboardButton(text="random_words", callback_data="random_words"),
            types.InlineKeyboardButton(text="study", callback_data="study")
        ]
    ])
    await message.answer("hi, what do you want to do?", reply_markup=keyboard)

@dp.callback_query(F.data == "settings")
async def quantity(callback: types.CallbackQuery):
    await callback.answer("settings")
    await callback.message.answer("/quantity your_number - quantity words\n /transc 1/0 - on/off transcription")

@dp.message(Command('transc'))
async def cmd_quantity(message: types.Message, command: CommandObject):
    data["config"]["transc"] = bool(int(command.args))
    print(bool(int(command.args)))
    print(data["config"]["transc"])
    update_data(data)
    await message.reply(f"transcription updated")

@dp.message(Command('quantity'))
async def cmd_quantity(message: types.Message, command: CommandObject):
    data["config"]["quantity_words"] = int(command.args)
    update_data(data)
    await message.reply(f"quantity updated")
                       
@dp.callback_query(F.data == "load_file")
async def load_file(callback: types.CallbackQuery):
    await callback.answer("load_file")
    await callback.message.answer("send me file")



@dp.callback_query(F.data == "random_words")
async def random_words(callback: types.CallbackQuery):
    await callback.answer("random_words")
    m = keybord_words(data, c, i)
    await callback.message.answer(m[0], reply_markup=m[1])



@dp.callback_query(F.data.startswith("yes_"))
async def yes(callback: types.CallbackQuery):
    await callback.answer()
    key_word = callback.data.split("_")[-1]
    change_data(data, True, key_word)
    print(key_word)
    global i
    i += 1
    if c < config['quantity_words']:
        await callback.answer("yes")
        m = keybord_words(data, c, i)
        await callback.message.edit_text(m[0], reply_markup=m[1])
        

@dp.callback_query(F.data.startswith("no_"))
async def no(callback: types.CallbackQuery):
    await callback.answer()
    key_word = callback.data.split("_")[-1]
    change_data(data, False, key_word)
    print(key_word)
    global i
    global c
    i += 1
    c += 1
    print(c)
    if c < config['quantity_words']:
        m = keybord_words(data, c, i)
        await callback.message.edit_text(m[0], reply_markup=m[1])
    else:
        keyboard  = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton(text="go to study", callback_data=f"study")
            ]
        ])
        await callback.message.edit_text(f"new words {c}/{c}", reply_markup=keyboard)
        c = 0
        i = 1
        return


@dp.callback_query(F.data == "study")
async def stady(callback: types.CallbackQuery):
    if word_list(data) != "":
        keyboard  = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton(text="go to repeat", callback_data=f"repeat")
            ]
        ])
        await callback.message.answer(word_list(data), reply_markup=keyboard)
        update_data(data)
    else:
        await callback.message.answer("not found new words")





@dp.message(F.document)
async def handle_document(message: types.Message):
    doc = message.document
    file_id = doc.file_id
    file_name = doc.file_name
    download_folder = "downloads"

    import os
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path
        download_path = os.path.join(download_folder, file_name)
        await bot.download_file(file_path, download_path)
        convert()
        await message.reply("success")
    except Exception as e:
        logging.error("error")
        await message.reply("error")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())