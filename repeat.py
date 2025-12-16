from aiogram import F, Router
from aiogram import types
from utils_r import keybord_words_r, print_word_r, repeat_list
from utils import change_data, print_word, create_keyboard
from data import get_data, update_data
from conf import bi
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

rr = Router()


class Data(StatesGroup):
    data = State()




@rr.callback_query(F.data == "repeat")
async def repeat(callback: types.CallbackQuery, state: FSMContext):
    data = get_data()  # Сначала получаем данные
    await state.update_data(data=data)  # Затем обновляем состояние
    current_state = await state.get_data()  # Получаем данные из состояния
    data = current_state.get("data") or data  # Если в состоянии нет данных, используем полученные
    bi.l = repeat_list(data)
    bi.i = 0
    bi.c = 0
    await callback.answer()
    m = keybord_words_r(data, bi.c)
    mes = f"{m[0]}\n{print_word_r(bi.l[bi.i], data)}"
    await callback.message.edit_text(text=mes, reply_markup=m[1])

@rr.callback_query(F.data == "continue")
async def continue_r(callback: types.CallbackQuery, state: FSMContext):
    data = get_data()  # Сначала получаем данные
    await state.update_data(data=data)  # Затем обновляем состояние
    current_state = await state.get_data()  # Получаем данные из состояния
    data = current_state.get("data") or data  # Если в состоянии нет данных, используем полученные
    await callback.answer()
    m = keybord_words_r(data, bi.c)
    print(bi.l, bi.l[bi.i])
    mes = f"{m[0]}\n{print_word(bi.l[bi.i], data)}"
    await callback.message.edit_text(text=mes, reply_markup=m[3])


@rr.callback_query(F.data.startswith("r-yes_"))
async def yes_r(callback: types.CallbackQuery, state: FSMContext):
    data = get_data()  # Сначала получаем данные
    await state.update_data(data=data)  # Затем обновляем состояние
    current_state = await state.get_data()  # Получаем данные из состояния
    data = current_state.get("data") or data  # Если в состоянии нет данных, используем полученные
    await callback.answer()
    key_word = bi.l[bi.i]
    change_data(data, True, key_word)
    
    # После изменения данных, получаем обновленные данные
    data = get_data()
    await state.update_data(data=data)
    
    print(bi.l, bi.l[bi.i])
    m = keybord_words_r(data, bi.c)
    bi.i += 1
    bi.c += 1
    if bi.i < len(bi.l):
        mes = f"{m[0]}\n{print_word_r(bi.l[bi.i], data)}"
        await callback.message.edit_text(mes, reply_markup=m[1])
    else:
        if bi.c == len(bi.l):
            await callback.message.edit_text(f"known words {bi.c}/{len(bi.l)}")
            keyboard = create_keyboard([["load_file", "settings"],["random_words", "study"], ["stats"]])
            await callback.message.answer("hi, what do you want to do?", reply_markup=keyboard)
            bi.l = repeat_list(data)
        else:
            update_data(data)
            keyboard = create_keyboard([["repeat"]])
            await callback.message.edit_text(f"known words {bi.c}/{len(bi.l)}", reply_markup=keyboard)
        bi.i = 0
        bi.c = 0
        
        return
        
@rr.callback_query(F.data.startswith("r-no_"))
async def no_r(callback: types.CallbackQuery, state: FSMContext):
    data = get_data()  # Сначала получаем данные
    await state.update_data(data=data)  # Затем обновляем состояние
    current_state = await state.get_data()  # Получаем данные из состояния
    data = current_state.get("data") or data  # Если в состоянии нет данных, используем полученные
    await callback.answer()
    print(bi.l, bi.l[bi.i])
    m = keybord_words_r(data, bi.c)
    bi.i += 1
    if bi.i < len(bi.l):
        mes = f"{m[0]}\n{print_word_r(bi.l[bi.i], data)}"
        await callback.message.edit_text(mes, reply_markup=m[1])
    else:
        update_data(data)
        keyboard = create_keyboard([["repeat"]])
        await callback.message.edit_text(f"known words {bi.c}/{len(bi.l)}", reply_markup=keyboard)
        bi.i = 0
        bi.c = 0
        return