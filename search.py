from aiogram import F, Router
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from data import get_data
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
    key_words = search_word(words, get_data())
    if key_words != []:
        mes1 = ""
        for w in key_words:
            mes1 += print_word(w, get_data())
        mes = "here is the word that was found:\n" + mes1 + "what do you want to do with it?"
        keyboard = create_keyboard([["edit", "delete"], ["add_in_dict"]])
        await message.answer(mes, reply_markup=keyboard)
    else:
        await message.answer("not found")
