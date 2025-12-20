from utils import choose_words, create_keyboard
from aiogram import types

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
    mes = f"which of these words do you know? (known words: {c}/{data['config']['quantity_words']})\n"
    mes2 = "did you answer correctly?"

    return [mes, keyboard, mes2, keyboard2]

