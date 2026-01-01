from utils.utils import create_keyboard
from utils.data import get_data
from utils.utils_s import words_list_s 
from utils.utils import create_keyboard, word_list
from utils.lang import M
from utils.callback import callback


async def stats_func(event):
    event = await callback(event)
    words = get_data()['words']
    message = f'{M('stats1')}{len(words)}\n{M('stats2')}{len(words_list_s(1))}\n{M('stats3')}{len(words_list_s(0))}'
    keybord = create_keyboard([['known', 'unknown']])
    await event.answer(message, reply_markup=keybord)


async def known_func(callback):
    await callback.answer()
    mes = word_list(get_data(), True)
    if mes != '':
        await callback.message.answer(mes)
    else:
        await callback.message.answer(M('not_found'))




async def unknown_func(callback):
    await callback.answer()
    mes = word_list(get_data(), False)
    if mes != '':
        await callback.message.answer(mes)
    else:
        await callback.message.answer(M('not_found'))