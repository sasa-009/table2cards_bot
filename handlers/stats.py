from aiogram import F, Router
from aiogram import types
from utils.utils import change_data, print_word, create_keyboard
from utils.data import get_data, update_data
from utils.conf import bi
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from utils.utils_s import words_list_s 
from utils.utils import create_keyboard, word_list
from utils.lang import M

rs = Router()

@rs.callback_query(F.data == "stats")
async def stats(callback: types.CallbackQuery):
    words = get_data()["words"]
    await callback.answer()
    message = f"{M('stats1')}{len(words)}\n{M('stats2')}{len(words_list_s(1))}\n{M('stats3')}{len(words_list_s(0))}"
    keybord = create_keyboard([["known", "unknown"]])
    await callback.message.answer(message, reply_markup=keybord)



@rs.callback_query(F.data == "known")
async def known(callback: types.CallbackQuery):
    await callback.answer()
    mes = word_list(get_data(), True)
    if mes != "":
        await callback.message.answer(mes)
    else:
        await callback.message.answer(M("not_found"))




@rs.callback_query(F.data == "unknown")
async def unknown(callback: types.CallbackQuery):
    await callback.answer()
    mes = word_list(get_data(), False)
    if mes != "":
        await callback.message.answer(mes)
    else:
        await callback.message.answer(M("not_found"))