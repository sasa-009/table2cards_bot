from aiogram import F, Router
from aiogram import types
from aiogram.filters.command import CommandStart, Command, CommandObject

from convert import convert
from utils import change_data, keybord_words, word_list, create_keyboard
from data import get_data, update_data

from utils_s import words_list_s 
from utils import create_keyboard, word_list

rm = Router()

i = 1
c = 0
data = get_data()
config = data['config']




@rm.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = create_keyboard([["load_file", "settings"],["random_words", "study"],["stats", "add_words"], ["search"]])
    await message.answer("hi, what do you want to do?", reply_markup=keyboard)


@rm.callback_query(F.data == "settings")
async def quantity(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("/quantity your_number - quantity words\n /transc 1/0 - on/off transcription")


@rm.message(Command('transc'))
async def cmd_quantity(message: types.Message, command: CommandObject):
    data["config"]["transc"] = bool(int(command.args))
    update_data(data)
    await message.reply(f"transcription updated")


@rm.message(Command('quantity'))
async def cmd_quantity(message: types.Message, command: CommandObject):
    data["config"]["quantity_words"] = int(command.args)
    update_data(data)
    await message.reply(f"quantity updated")


@rm.callback_query(F.data == "load_file")
async def load_file(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("send me file")



@rm.callback_query(F.data == "random_words")
async def random_words(callback: types.CallbackQuery):
    await callback.answer()
    m = keybord_words(data, c, i)
    await callback.message.answer(m[0], reply_markup=m[1])



@rm.callback_query(F.data.startswith("yes_"))
async def yes(callback: types.CallbackQuery):
    await callback.answer()
    key_word = callback.data.split("_")[-1]
    data = change_data(data, True, key_word)
    print(key_word)
    global i
    i += 1
    if c < config['quantity_words']:
        await callback.answer()
        m = keybord_words(data, c, i)
        await callback.message.edit_text(m[0], reply_markup=m[1])
        

@rm.callback_query(F.data.startswith("no_"))
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
        keyboard = create_keyboard([["study"]])
        await callback.message.edit_text(f"new words {c}/{c}", reply_markup=keyboard)
        c = 0
        i = 1
        return


@rm.callback_query(F.data == "study")
async def stady(callback: types.CallbackQuery):
    data = get_data()
    await callback.answer()
    if word_list(data, False) != "":
        keyboard = create_keyboard([["repeat"]])
        await callback.message.answer(word_list(data, False), reply_markup=keyboard)
        update_data(data)
    else:
        await callback.message.answer("not found new words")


@rm.message(F.document)
async def handle_document(message: types.Message):
    doc = message.document
    file_id = doc.file_id
    file_name = doc.file_name
    download_folder = "downloads"

    import os
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        file_info = await message.bot.get_file(file_id)
        file_path = file_info.file_path
        download_path = os.path.join(download_folder, file_name)
        await message.bot.download_file(file_path, download_path)
        convert()
        await message.reply("success")
    except Exception:
        await message.reply("error")


# @rm.callback_query(F.data == "stats")
# async def stats(callback: types.CallbackQuery):
#     await callback.answer()
#     message = f"""
# All words: {len(get_data()) - 1}
# 1. Known words: {len(words_list_s(1))}
# 2. Unknown words: {len(words_list_s(0))}
# """
#     keybord = create_keyboard([["known", "unknown"]])
#     await callback.message.answer(message, reply_markup=keybord)


# @rm.callback_query(F.data == "known")
# async def known(callback: types.CallbackQuery):
#     await callback.answer()
#     await callback.message.answer("known words:\n" + word_list(get_data(), True))


# @rm.callback_query(F.data == "unknown")
# async def unknown(callback: types.CallbackQuery):
#     await callback.message.answer("unknown words:\n" + word_list(get_data(), False))
#     await callback.answer()