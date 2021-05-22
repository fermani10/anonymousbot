from pyrogram import (
    Client,
    filters
    )

MESSAGE = """No disponible
"""


@Client.on_message(filters.group)
async def leave(client, message):
    await message.reply_text(MESSAGE)
    await message.chat.leave()
