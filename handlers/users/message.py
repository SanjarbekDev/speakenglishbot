from aiogram import types
from loader import dp

from oxfordloockup import get_definitions
from gtranslator import translator, detect_lang


@dp.message_handler(content_types='text')
async def message(message: types.Message):
    if len(message.text.split())>2:
        await message.answer(translator(message.text))
    else:
        if detect_lang(message.text)=='en':
            word_id=message.text
        else:
            word_id=translator(message.text)
        lokup=get_definitions(word_id)
        if lokup:
            await message.answer(f"word id: {word_id},\nDefinition: {lokup['definition']}")
            if lokup.get('audio'):
                await message.reply_voice(lokup['audio'])

        else:
            await message.answer("Bunday so'z topilmadi")
        