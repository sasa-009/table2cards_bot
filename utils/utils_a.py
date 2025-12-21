from utils.data import update_data


def add_word(words, data):

    words = words.splitlines()
    for w in words:
        try:
            word = {
                "word": None,
                "transc": None,
                "transl": None,
                "learn": None,
                "rd": None,
                "rdl": None,
                "known": None,
                "tags": [],
            }
            l = w.split("-")
            word["word"] = "  "+l[0].strip()+"  "
            word["transc"] = "  "+l[1].strip()+"  "
            word["transl"] = "  "+l[2].strip()+"  "
            key_word = int(list(data["words"].keys())[-1])
            key_word += 1
            data["words"][key_word] = word
            update_data(data)
        except:
            return False