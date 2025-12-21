from aiogram import F, Router
from aiogram import types
from aiogram.filters.command import CommandStart, Command, CommandObject

from convert import convert
from utils.utils import change_data, keybord_words, word_list, create_keyboard
from utils.data import get_data, update_data

from utils.utils_s import words_list_s 
from utils.utils import create_keyboard, word_list

from utils.lang import M

rm = Router()

i = 1
c = 0
data = get_data()
config = data['config']




@rm.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = create_keyboard([["load_file", "settings"],["random_words", "study"],["stats", "add_words"], ["search", "tags"]])
    await message.answer(M("start"), reply_markup=keyboard)


@rm.callback_query(F.data == "settings")
async def settings(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(M("settings"))


@rm.message(Command('transc'))
async def cmd_transc(message: types.Message, command: CommandObject):
    data["config"]["transc"] = bool(int(command.args))
    update_data(data)
    await message.reply(M("cmd_transc"))


@rm.message(Command('quantity'))
async def cmd_quantity(message: types.Message, command: CommandObject):
    data["config"]["quantity_words"] = int(command.args)
    update_data(data)
    await message.reply(M("cmd_quantity"))


@rm.message(Command('lang'))
async def cmd_lang(message: types.Message, command: CommandObject):
    data["config"]["lang"] = command.args
    update_data(data)
    await message.reply(M("cmd_lang"))


@rm.callback_query(F.data == "load_file")
async def load_file(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(M("load_file"))


@rm.callback_query(F.data == "random_words")
async def random_words(callback: types.CallbackQuery):
    await callback.answer()
    m = keybord_words(data, c, i)
    await callback.message.answer(m[0], reply_markup=m[1])



@rm.callback_query(F.data.startswith("yes_"))
async def yes(callback: types.CallbackQuery):
    await callback.answer()
    key_word = callback.data.split("_")[-1]
    change_data(data, True, key_word)
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
    global i
    global c
    i += 1
    c += 1
    if c < config['quantity_words']:
        m = keybord_words(data, c, i)
        await callback.message.edit_text(m[0], reply_markup=m[1])
    else:
        keyboard = create_keyboard([["study"]])
        await callback.message.edit_text(f"{M('rw_no')}{c}/{c}", reply_markup=keyboard)
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
        await callback.message.answer(M("stady"))


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
        await message.reply(M("success"))
    except Exception:
        await message.reply(M("error"))


