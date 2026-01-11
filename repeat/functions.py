from utils.utils_r import keybord_words_r, print_word_r, repeat_list
from utils.utils import change_data, print_word, create_keyboard, change_repeat_date
from utils.data import get_data, update_data
from utils.conf import bi
from utils.lang import M
from utils.callback import callback
from utils.utils import word_list_repeat


async def study_func(event):
    data = get_data()
    event = await callback(event)
    key_words = repeat_list(data)
    if key_words != []:
        keyboard = create_keyboard([['repeat']])
        await event.answer(word_list_repeat(data, key_words), reply_markup=keyboard)
        update_data(data)
    else:
        await event.answer(M('study'))


async def repeat_func(event):
    event = await callback(event)
    data = get_data()
    bi.l = repeat_list(data)
    bi.i = 0
    bi.c = 0
    m = keybord_words_r(data, bi.c)
    mes = f'{m[0]}\n{print_word_r(bi.l[bi.i], data)}'
    await event.edit_text(text=mes, reply_markup=m[1])


async def continue_r_func(callback):
    await callback.answer()
    data = get_data() 
    m = keybord_words_r(data, bi.c)
    mes = f'{m[0]}\n{print_word(bi.l[bi.i], data)}'
    await callback.message.edit_text(text=mes, reply_markup=m[3])


async def yes_r_func(callback):
    await callback.answer()
    data = get_data()
    key_word = bi.l[bi.i]
    # change_data(data, True, key_word)
    change_repeat_date(data, key_word)
    data = get_data()
    m = keybord_words_r(data, bi.c)
    bi.i += 1
    bi.c += 1
    if bi.i < len(bi.l):
        mes = f'{m[0]}\n{print_word_r(bi.l[bi.i], data)}'
        await callback.message.edit_text(mes, reply_markup=m[1])
    else:
        if bi.c == len(bi.l):
            await callback.message.edit_text(f'{M('repeat_kw')}{bi.c}/{len(bi.l)}')
            bi.l = repeat_list(data)
        else:
            update_data(data)
            keyboard = create_keyboard([['repeat']])
            await callback.message.edit_text(f'{M('repeat_kw')}{bi.c}/{len(bi.l)}', reply_markup=keyboard)
        bi.i = 0
        bi.c = 0
        
        return
        
async def no_r_func(callback):
    await callback.answer()
    data = get_data() 
    m = keybord_words_r(data, bi.c)
    bi.i += 1
    if bi.i < len(bi.l):
        mes = f'{m[0]}\n{print_word_r(bi.l[bi.i], data)}'
        await callback.message.edit_text(mes, reply_markup=m[1])
    else:
        update_data(data)
        keyboard = create_keyboard([['repeat']])
        await callback.message.edit_text(f'{M('repeat_kw')}{bi.c}/{len(bi.l)}', reply_markup=keyboard)
        bi.i = 0
        bi.c = 0
        return