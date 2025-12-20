from aiogram import F, Router
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from data import get_data, update_data
from utils import print_word, create_keyboard
from utils_srh import search_word
from conf import bi

rsrh = Router()


class Search(StatesGroup):
    word = State()
    edit = State()


@rsrh.callback_query(F.data == "search")
async def start_search(callbeck: types.CallbackQuery, state: FSMContext):
    await callbeck.answer()
    mes = "send me word"
    await state.set_state(Search.word)
    await callbeck.message.answer(mes)


@rsrh.message(Search.word)
async def search(message: types.message, state: FSMContext):
    await state.update_data(word=message.text)
    data = await state.get_data()
    words = data["word"]
    key_words = search_word(words)
    if key_words != []:
        mes1 = ""
        for w in key_words:
            mes1 += print_word(w, get_data())
        mes = "here is the word that was found:\n" + mes1 + "what do you want to do with it?"
        keyboard = create_keyboard([["edit", "delete"], ["add_in_dict"]])
        await message.answer(mes, reply_markup=keyboard)
    else:
        await message.answer("not found")


@rsrh.callback_query(F.data == "edit")
async def edit(callback: types.CallbackQuery, state: FSMContext):
    callback.answer()
    data = await state.get_data()
    words = data["word"]
    key_words = search_word(words)
    mes = "write a new version of this word in the following format:\nword - transcription - translation\n"+print_word(key_words[bi.k], get_data())
    await callback.message.answer(mes)
    await state.set_state(Search.edit)
    bi.kw = key_words


@rsrh.message(Search.edit)
async def get_edit(message: types.message, state: FSMContext):
    key_words = bi.kw
    data2 = get_data()
    keyboard  = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="next", callback_data=f"edit")
        ]
    ])
    word = {
        "word": None,
        "transc": None,
        "transl": None,
        "learn": None,
        "rd": None,
        "rdl": None,
        "known": None,
        "tags": [],
    }
    await state.update_data(edit=message.text)
    data = await state.get_data()
    edit = data["edit"]
    print(edit)
    l = edit.split("-")
    word["word"] = "  "+l[0].strip()+"  "
    word["transc"] = "  "+l[1].strip()+"  "
    word["transl"] = "  "+l[2].strip()+"  "
    data2["words"][key_words[bi.k]] = word
    update_data(data2)

    # await callback.message.answer("error, try again", reply_markup=keyboard)
    if bi.k < len(key_words) - 1:
        bi.k += 1
        await message.answer("success", reply_markup=keyboard)
    else:
        await message.answer("success")


@rsrh.callback_query(F.data == "delete")
async def delete(callbeck: types.CallbackQuery, state: FSMContext):
    callbeck.answer()
    data = await state.get_data()
    words = data["word"]
    key_words = search_word(words)
    data2 = get_data()
    for i in key_words:
        data2["words"].pop(i, None)
    update_data(data2)
    await callbeck.message.answer("success")