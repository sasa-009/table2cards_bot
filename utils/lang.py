import json
from utils.data import get_data

def get_messages():
    data = get_data()
    lang = data["config"]["lang"]
    if lang == "ru":
        with open("messages_ru.json", "r", encoding="utf-8") as f:
            mes = json.load(f)
    if lang == "en":
        with open("messages_en.json", "r", encoding="utf-8") as f:
            mes = json.load(f)
    return mes



def M(key):
    mes = get_messages()
    return mes[key]