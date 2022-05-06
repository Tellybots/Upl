


import os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.add import add_user_to_database
from functions.forcesub import handle_force_subscribe

f = filters.command("start")

@Client.on_message(f)
async def start(c, m):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_message(
        Config.LOG_CHANNEL,
           f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) started @{Config.BOT_USERNAME} !!"
    )
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(c, m)
      if fsub == 400:
        return
    await update.reply_text(
        text=Translation.START_TEXT.format(m.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )
    print("start")
