from utils.callback import callback
from utils.lang import M
from convert import convert


async def load_file_func(event):
    event = await callback(event)
    await event.answer(M('load_file'))

async def handle_document_func(message):
    doc = message.document
    file_id = doc.file_id
    file_name = doc.file_name
    download_folder = 'downloads'

    import os
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        file_info = await message.bot.get_file(file_id)
        file_path = file_info.file_path
        download_path = os.path.join(download_folder, file_name)
        await message.bot.download_file(file_path, download_path)
        convert()
        await message.reply(M('success'))
    except Exception:
        await message.reply(M('error'))


