from utils.data import get_data
from utils.utils_r import repeat_list


class BotInstance:
    def __init__(self):
        self.i = 0
        self.c = 0
        self.k = 0
        self.kw = 0
        self.l = repeat_list(get_data())


        
    
bi = BotInstance()
