
from utils.data import get_data, update_data
from utils.lang import M
from utils.callback import callback

data = get_data()

async def settings_func(event):
    message = await callback(event)
    await message.answer(M("settings"))


async def cmd_transc_func(message, command):
    data["config"]["transc"] = bool(int(command.args))
    update_data(data)
    await message.reply(M("cmd_transc"))


async def cmd_quantity_func(message, command):
    data["config"]["quantity_words"] = int(command.args)
    update_data(data)
    await message.reply(M("cmd_quantity"))


async def cmd_lang_func(message, command):
    data["config"]["lang"] = command.args
    update_data(data)
    await message.reply(M("cmd_lang"))