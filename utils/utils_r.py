from utils.utils import choose_words, create_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.lang import M
from datetime import date

def repeat_list(data):
    today = date.today()
    l = []
    for i in data['words']:
        if data['words'][i]['repeat_date'] == str(today):
            l.append(i)
    return l


def print_word_r(key_word, data):
    word = data['words'][key_word]
    return f'{word['word']}\n'


def keybord_words_r(data, c):
    key_word = choose_words(data)

    keyboard = create_keyboard([['continue']])
    keyboard2  = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='✅', callback_data=f'r-yes_{key_word}'),
            InlineKeyboardButton(text='❌', callback_data=f'r-no_{key_word}')
        ]
    ])
    mes = f'{M('repeat')}{c}/{data['config']['quantity_words']})\n'
    mes2 = M('repeat2')

    return [mes, keyboard, mes2, keyboard2]