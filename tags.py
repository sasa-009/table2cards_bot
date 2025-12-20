from aiogram import F, Router
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from data import get_data, update_data
from utils import print_word, create_keyboard
from utils_srh import search_word, search_word_tag
from conf import bi

rt = Router()


class Tags(StatesGroup):
    create = State()
    delete = State()
    add = State()


@rt.callback_query(F.data == "tags")
async def tags(callbeck: types.CallbackQuery):
    await callbeck.answer()
    keyboard = create_keyboard([["create_tag", "delete_tag"], ["tag_list"]])
    mes = "what do you want to do?"
    await callbeck.message.answer(mes, reply_markup=keyboard)


@rt.callback_query(F.data == "create_tag")
async def create_tag(callbeck: types.CallbackQuery, state: FSMContext):
    await callbeck.answer()
    mes = "enter the tag name"
    await callbeck.message.answer(mes)
    await state.set_state(Tags.create)

@rt.message(Tags.create)
async def create_tag_(message: types.Message, state: FSMContext):
    data = get_data()
    data["tags"].append(message.text)
    update_data(data)
    await message.answer("success")

@rt.callback_query(F.data == "delete_tag")
async def delete_tag(callbeck: types.CallbackQuery, state: FSMContext):
    await callbeck.answer()
    mes = "enter the tag name"
    await callbeck.message.answer(mes)
    await state.set_state(Tags.delete)

@rt.message(Tags.delete)
async def delete_tag_(message: types.Message, state: FSMContext):
    data = get_data()
    data["tags"].remove(message.text)
    key_words = search_word_tag(message.text)
    for k in key_words:
        data["words"][k]["tags"].remove(message.text)
    update_data(data)
    await message.answer("success")



@rt.callback_query(F.data == "tag_list")
async def tag_list(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    data = get_data()
    tags = data["tags"]
    kl = []
    for t in tags:
        kl.append(["tag:"+t])
    keyboard = create_keyboard(kl)
    if tags != []:
        await callback.message.answer("choose tag", reply_markup=keyboard)
    else:
        await callback.message.answer("not found")

@rt.callback_query(F.data.startswith("tag:"))
async def tag_(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    tag = callback.data.split(":")[-1]
    await state.update_data(add=tag)
    keyboard = create_keyboard([["delete_tag", "add_tag_2_words"]])
    mes = ""
    key_words = search_word_tag(tag)
    for i in key_words:
        mes += print_word(i, get_data())

    await callback.message.answer("what do you want to do?\n"+mes, reply_markup=keyboard)


@rt.callback_query(F.data == "add_tag_2_words")
async def add_tag_2_words(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("which words to add tag?")
    await state.set_state(Tags.add)


@rt.message(Tags.add)
async def add_tag(message: types.Message, state: FSMContext):
    data_tag = await state.get_data()
    tag = data_tag["add"]
    data = get_data()
    key_words = search_word(message.text)
    for k in key_words:
        data["words"][k]["tags"].append(tag)
    update_data(data)
    await message.answer("success")