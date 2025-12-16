# from aiogram import F, Router
# from aiogram import types
# from utils_r import keybord_words_r, print_word_r, repeat_list
# from utils import change_data, print_word, create_keyboard
# from data import get_data, update_data
# from conf import bi
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext



# rs = Router()
# from utils_s import words_list_s 
# from utils import create_keyboard, word_list

# @rs.callback_query(F.data == "stats")
# async def stats(callback: types.CallbackQuery):
#     callback.answer()
#     message = f"""
# All words: {len(get_data()) - 1}
# 1. Known words: {len(words_list_s(1))}
# 2. Unknown words: {len(words_list_s(0))}
# """
#     keybord = create_keyboard([["known", "unknown"]])
#     callback.message.answer(message, reply_markup=keybord)



# @rs.callback_query(F.data == "known")
# async def known(callback: types.CallbackQuery):
#     callback.answer()
#     callback.message.answer(word_list(get_data(), True))




# @rs.callback_query(F.data == "unknown")
# async def unknown(callback: types.CallbackQuery):
#     callback.answer()
#     callback.message.answer(word_list(get_data(), False))