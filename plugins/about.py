import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5793472760:AAE2N3-RFo0V-8S87fke4iCROCWjRS3kWrc')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"ᴀʙᴏᴜᴛ 🏆 :- <a href='https://t.me/movie_timebot_only'>🏆ᴛʀᴜᴍʙᴏᴛs🏆</a>\nCreater :- <a href='https://t.me/Fligher'>🌘ғʟɪɢʜᴇʀ🌒</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- KOYEB\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/mrmalik_offl'>ᴍʀ.ᴍᴀʟɪᴋ</a>** for your contribution \n\n❤️ I support you **<a href='https://t.me/mrmalik_offl'>ᴍʀ.ᴍᴀʟɪᴋ</a>** ❤️",quote=True)
