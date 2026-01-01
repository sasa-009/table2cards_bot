from utils.data import get_data, update_data
from utils.utils import print_word, create_keyboard
from utils.utils_srh import search_word, search_word_tag
from utils.lang import M
from utils.callback import callback
from utils.states import Tags



async def tags_func(event):
    event = await callback(event)
    keyboard = create_keyboard([['create_tag', 'delete_tag'], ['tag_list']])
    mes = M('tags')
    await event.answer(mes, reply_markup=keyboard)


async def create_tag_func(callback, state):
    await callback.answer()
    mes = M('tag_name')
    await callback.message.edit_text(mes)
    await state.set_state(Tags.create)

async def create_tag__func(message):
    data = get_data()
    data['tags'].append(message.text)
    update_data(data)
    await message.answer(M('success'))

async def delete_tag_func(callback, state):
    await callback.answer()
    mes = M('tag_name')
    await callback.message.edit_text(mes)
    await state.set_state(Tags.delete)

async def delete_tag__func(message):
    data = get_data()
    data['tags'].remove(message.text)
    key_words = search_word_tag(message.text)
    for k in key_words:
        data['words'][k]['tags'].remove(message.text)
    update_data(data)
    await message.answer(M('success'))



async def tag_list_func(callback):
    await callback.answer()
    data = get_data()
    tags = data['tags']
    kl = []
    for t in tags:
        kl.append(['tag:'+t])
    keyboard = create_keyboard(kl)
    if tags != []:
        await callback.message.edit_text(M('tag_list'), reply_markup=keyboard)
    else:
        await callback.message.edit_text(M('not_found'))

async def tag__func(callback, state):
    await callback.answer()
    tag = callback.data.split(':')[-1]
    await state.update_data(add=tag)
    keyboard = create_keyboard([['delete_tag', 'add_tag_2_words']])
    mes = ''
    key_words = search_word_tag(tag)
    for i in key_words:
        mes += print_word(i, get_data())

    await callback.message.edit_text(f'{M('tags')}\n{mes}', reply_markup=keyboard)


async def add_tag_2_words_func(callback, state):
    await callback.answer()
    await callback.message.edit_text(M('add_tag_2_words'))
    await state.set_state(Tags.add)


async def add_tag_func(message, state):
    data_tag = await state.get_data()
    tag = data_tag['add']
    data = get_data()
    key_words = search_word(message.text)
    for k in key_words:
        data['words'][k]['tags'].append(tag)
    update_data(data)
    await message.answer(M('success'))