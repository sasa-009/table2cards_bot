from aiogram import F, Router
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from utils.utils_a import add_word
from utils.data import get_data
from utils.lang import M

ra = Router()


class Words(StatesGroup):
    mes_words = State()



@ra.callback_query(F.data == "add_words")
async def add_words(callbeck: types.CallbackQuery, state: FSMContext):
    await callbeck.answer()
    mes = M("add_words")
    await state.set_state(Words.mes_words)
    await callbeck.message.answer(mes)


@ra.message(Words.mes_words)
async def get_word(message: types.message, state: FSMContext):
    await state.update_data(mes_words=message.text)
    data = await state.get_data()
    words = data["mes_words"]
    res_add = add_word(words, get_data())
    if res_add != False:
        await message.answer(M("success"))
    else:
        await message.answer(M("error"))
