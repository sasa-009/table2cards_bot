from data import get_data



def words_list_s(atr = None):
    data = get_data()
    unknown_list = []
    know_list = []
    for i in data["words"]:
        if i != "config":
            key_word = i
            if data["words"][key_word]["known"] == True:
                know_list.append(key_word)
            elif data["words"][key_word]["known"] == False:
                unknown_list.append(key_word)
    if atr == 0:
        return unknown_list
    elif atr == 1:
        return know_list
    elif atr == None:
        all_list = unknown_list + know_list
        return all_list