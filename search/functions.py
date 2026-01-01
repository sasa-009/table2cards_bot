from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.data import get_data, update_data
from utils.utils import print_word, create_keyboard
from utils.utils_srh import search_word
from utils.conf import bi
from utils.lang import M
from utils.states import Search
from utils.callback import callback




async def start_search_func(event, state):
    event = await callback(event)
    mes = M('start_search')
    await state.set_state(Search.word)
    await event.answer(mes)


async def search_func(message, state):
    await state.update_data(word=message.text)
    data = await state.get_data()
    words = data['word']
    key_words = search_word(words)
    if key_words != []:
        mes1 = ''
        for w in key_words:
            mes1 += print_word(w, get_data())
        mes = M('search') + mes1 + M('search2')
        keyboard = create_keyboard([['edit', 'delete'], ['add_in_dict']])
        await message.answer(mes, reply_markup=keyboard)
    else:
        await message.answer(M('not_found'))


async def edit_func(callback, state):
    callback.answer()
    data = await state.get_data()
    words = data['word']
    key_words = search_word(words)
    mes = M('edit')+print_word(key_words[bi.k], get_data())
    await callback.message.answer(mes)
    await state.set_state(Search.edit)
    bi.kw = key_words


async def get_edit_func(message, state):
    key_words = bi.kw
    data2 = get_data()
    keyboard  = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='next', callback_data=f'edit')
        ]
    ])
    word = {
        'word': None,
        'transc': None,
        'transl': None,
        'learn': None,
        'rd': None,
        'rdl': None,
        'known': None,
        'tags': [],
    }
    await state.update_data(edit=message.text)
    data = await state.get_data()
    edit = data['edit']
    print(edit)
    l = edit.split('-')
    word['word'] = '  '+l[0].strip()+'  '
    word['transc'] = '  '+l[1].strip()+'  '
    word['transl'] = '  '+l[2].strip()+'  '
    data2['words'][key_words[bi.k]] = word
    update_data(data2)

    # await callback.message.answer('error, try again', reply_markup=keyboard)
    if bi.k < len(key_words) - 1:
        bi.k += 1
        await message.answer(M('success'), reply_markup=keyboard)
    else:
        await message.answer(M('success'))


async def delete_func(callback, state):
    callback.answer()
    data = await state.get_data()
    words = data['word']
    key_words = search_word(words)
    data2 = get_data()
    for i in key_words:
        data2['words'].pop(i, None)
    update_data(data2)
    await callback.message.answer(M('success'))