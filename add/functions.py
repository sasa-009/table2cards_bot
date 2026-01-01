from aiogram.fsm.state import StatesGroup, State
from utils.utils_a import add_word
from utils.data import get_data
from utils.lang import M
from utils.callback import callback



class Words(StatesGroup):
    mes_words = State()


async def add_words_func(event, state):
    event = await callback(event)
    mes = M('add_words')
    await state.set_state(Words.mes_words)
    await event.answer(mes)


async def get_word_func(event, state):
    await state.update_data(mes_words=event.text)
    data = await state.get_data()
    words = data['mes_words']
    res_add = add_word(words, get_data())
    if res_add != False:
        await event.answer(M('success'))
    else:
        await event.answer(M('error'))
