from data import get_data
from utils_r import repeat_list


class BotInstance:
    def __init__(self):
        self.i = 0
        self.c = 0
        self.l = repeat_list(get_data())


        
    
bi = BotInstance()
