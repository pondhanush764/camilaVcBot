from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hey 😡😡.\nYar nenga😬\nHello its clear in my bio, 'No pm'\n Any queries or any prblm visit @kittysupport 😡.\nWant gban?, Now get out of here or confirm gban🥱")
  return                        
