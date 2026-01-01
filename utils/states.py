from aiogram.fsm.state import StatesGroup, State


class Search(StatesGroup):
    word = State()
    edit = State()


class Tags(StatesGroup):
    create = State()
    delete = State()
    add = State()