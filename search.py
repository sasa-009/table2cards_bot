from aiogram import F, Router
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from data import get_data, update_data
from utils import print_word, create_keyboard
from utils_srh import search_word


class Search(StatesGroup):
    word = State()

rsrh = Router()

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
    await state.update_data(word=key_words)
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
async def edit(callbeck: types.CallbackQuery, state: FSMContext):
    pass



@rsrh.callback_query(F.data == "delete")
async def delete(callbeck: types.CallbackQuery, state: FSMContext):
    callbeck.answer()
    data = await state.get_data()
    words = data["word"]
    data2 = get_data()
    for i in words:
        data2.pop(i, None)
    update_data(data2)
    await callbeck.message.answer("success")