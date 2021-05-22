from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hola, soy **ANONYMOUS REMITENTE BOT.**\n
Solo reenvíeme algunos mensajes o
medios y yo ** los voy a Anonimizar** !!

~ Creado por @Facu para Maria.
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("👥 Grupo del Creador",
                          url="https://t.me/botnovedades")],
    [InlineKeyboardButton("💳 Donar al Creador 🥺",
                          url="https://t.me/botnovedades/89")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
