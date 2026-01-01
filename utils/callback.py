from aiogram.types import Message, CallbackQuery


async def callback(event, state=None):
    if isinstance(event, Message):
        # if state != None:
        #     return [event, state]
        # else:    
        #     return event
        return event
    if isinstance(event, CallbackQuery):
        await event.answer()
        # if state != None:
        #     return [event.message, state]
        # else:    
        #     return event.message
        return event.message
