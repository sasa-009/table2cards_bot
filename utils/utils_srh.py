from utils.data import get_data

def search_word(words):
    data = get_data()
    key_words = []
    words = words.replace(' ', '')
    words = words.split(",")
    for w in words:
        w_key_words = []
        for i in data["words"]:
            try:
                if " "+w+" " in data["words"][i]["word"]:
                    w_key_words.append(i)
            except:
                pass         
        w2_key_words = []
        k = 0
        if w_key_words != []:
            for j in w_key_words:
                w2_key_words.append(len(data["words"][j]["word"]))
                k += 1
            key_words.append(w_key_words[w2_key_words.index(min(w2_key_words))])
    return key_words
            
def search_word_tag(tag):
    data = get_data()
    key_words = []
    for i in data["words"]:
        if tag in data["words"][i]["tags"]:
            key_words.append(i)
    return key_words



