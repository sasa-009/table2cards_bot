import random as r
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.data import update_data
from utils.lang import M
from datetime import date, datetime, timedelta

def change_data(data, status, key_word):
    data['words'][key_word]['known'] = status
    update_data(data)    

def change_repeat_date(data, key_word):
    repeat_after = data['words'][key_word]['repeat_after']
    today = date.today()
    repeat_date = None

    if repeat_after == None:
        repeat_date = str(today+timedelta(days=1))
        data['words'][key_word]['repeat_after'] = 1
    elif repeat_after == 30:
        repeat_date = None
        change_data(data, True, key_word)
    else:
        interval_repeat = data['config']['interval_repeat']
        interval_index = interval_repeat.index(repeat_after)
        repeat_after = interval_repeat[interval_index+1]
        data['words'][key_word]['repeat_after'] = repeat_after
        repeat_date = str(today+timedelta(days=repeat_after))
    data['words'][key_word]['repeat_date'] = repeat_date
    update_data(data)



def print_word(key_word, data):
    word = data['words'][key_word]
    if data['config']['transc']:
        return f'{word['word']} ({word['transc']}) - {word['transl']}\n'
    else:
        return f'{word['word']} - {word['transl']}\n'


def choose_words(data):
    while True:
        key_word = str(r.randint(1, int(list(data['words'].keys())[-1])))
        if key_word in data['words'] and data['words'][key_word]['known'] == None:
            return key_word
        else:
            continue


def keybord_words(data, c, i):
        key_word = choose_words(data)

        keyboard  = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='✅', callback_data=f'yes_{key_word}'),
                InlineKeyboardButton(text='❌', callback_data=f'no_{key_word}')
            ]
        ])
        mes = f'{M('random_words')}{c}/{data['config']['quantity_words']})\n{i}. {print_word(key_word,data)}'
        return [mes, keyboard]




def word_list(data, status):
    mes = ''
    for i in data['words']:
        if data['words'][i]['known'] == status:
            mes += print_word(i, data)
    return mes


def word_list_repeat(data, key_words):
    mes = ''
    for i in key_words:
        mes += print_word(i, data)
    return mes    

def create_keyboard(names):
    for i in range(len(names)):
        for j in range(len(names[i])):
            name = names[i][j]
            names[i][j] = InlineKeyboardButton(text=name, callback_data=name)
    keyboard = InlineKeyboardMarkup(inline_keyboard=names)
    
    return keyboard

