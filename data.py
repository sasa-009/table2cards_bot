import json


def get_data():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def update_data(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

