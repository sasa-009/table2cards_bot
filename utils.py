import random as r
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import update_data


def change_data(data, status, key_word):
    data[key_word]['known'] = status
    return update_data(data)    



def print_word(key_word, data):
    word = data[key_word]
    if data["config"]["transc"]:
        return f'{word['word']} ({word['transc']}) - {word['transl']}\n'
    else:
        return f'{word['word']} - {word['transl']}\n'


def choose_words(data):
    return str(r.randint(1, len(data)-1))


def keybord_words(data, c, i):
        key_word = choose_words(data)

        keyboard  = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="✅", callback_data=f"yes_{key_word}"),
                InlineKeyboardButton(text="❌", callback_data=f"no_{key_word}")
            ]
        ])
        mes = f"which of these words do you know? (new words: {c}/{data['config']['quantity_words']})\n{i}. {print_word(key_word,data)}"
        return [mes, keyboard]




def word_list(data):
    mes = ""
    print(data[str(1)]["known"])
    for i in range(1, len(data)-1):
        if data[str(i)]["known"] == False:
            mes += print_word(str(i), data)
    return mes
    

def create_keyboard(names):
    for i in range(len(names)):
        for j in range(len(names[i])):
            name = names[i][j]
            names[i][j] = InlineKeyboardButton(text=name, callback_data=name)
    keyboard = InlineKeyboardMarkup(inline_keyboard=names)
    
    return keyboard