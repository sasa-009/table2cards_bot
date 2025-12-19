from data import get_data

def search_word(words):
    data = get_data()
    key_words = []
    words = words.replace(' ', '')
    words = words.split(",")
    for w in words:
        w_key_words = []
        for i in data:
            try:
                if " "+w+" " in data[i]["word"]:
                    w_key_words.append(i)
            except:
                pass         
        w2_key_words = []
        k = 0
        if w_key_words != []:
            for j in w_key_words:
                w2_key_words.append(len(data[j]["word"]))
                k += 1
            key_words.append(w_key_words[w2_key_words.index(min(w2_key_words))])
   

    return key_words
            




