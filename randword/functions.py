from utils.utils import change_data, keybord_words, create_keyboard
from utils.data import get_data, update_data
from utils.lang import M
from utils.callback import callback

from datetime import date

i = 1
c = 0


async def random_words_func(event):
    message = await callback(event)
    m = keybord_words(get_data(), c, i)
    await message.answer(m[0], reply_markup=m[1])


async def yes_func(callback):
    await callback.answer()
    data = get_data()
    key_word = callback.data.split('_')[-1]
    change_data(get_data(), True, key_word)
    global i
    i += 1
    if c < data['config']['quantity_words']:
        await callback.answer()
        m = keybord_words(data, c, i)
        await callback.message.edit_text(m[0], reply_markup=m[1])
    

async def no_func(callback):
    await callback.answer()
    data = get_data()
    key_word = callback.data.split('_')[-1]
    change_data(data, False, key_word)
    data['words'][key_word]['repeat_date'] = str(date.today())
    data = update_data(data)
    global i
    global c
    i += 1
    c += 1
    if c < data['config']['quantity_words']:
        m = keybord_words(data, c, i)
        await callback.message.edit_text(m[0], reply_markup=m[1])
    else:
        keyboard = create_keyboard([['study']])
        await callback.message.edit_text(f'{M('rw_no')}{c}/{c}', reply_markup=keyboard)
        c = 0
        i = 1
        return