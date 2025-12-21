from utils.utils import choose_words, create_keyboard
from aiogram import types
from utils.lang import M

def repeat_list(data):
    l = []
    for i in data["words"]:
        if i != "config":
            if data["words"][i]["known"] == False:
                l.append(i)
    return l


def print_word_r(key_word, data):
    word = data["words"][key_word]
    return f'{word['word']}\n'


def keybord_words_r(data, c):
    key_word = choose_words(data)

    keyboard = create_keyboard([["continue"]])
    keyboard2  = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="✅", callback_data=f"r-yes_{key_word}"),
            types.InlineKeyboardButton(text="❌", callback_data=f"r-no_{key_word}")
        ]
    ])
    mes = f"{M('repeat')}{c}/{data['config']['quantity_words']})\n"
    mes2 = M('repeat2')

    return [mes, keyboard, mes2, keyboard2]

