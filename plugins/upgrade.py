"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 70  ind /🌎 1$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 150  ind /🌎 2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 225  ind /🌎 3$  per Month
	
	
	Pay Using ```Gpay,PhonePe,GooglePlayReedem```
	
	After Payment Send Screenshots Of 
        Payment To Admin @fligher"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/fligher")], 
        			[InlineKeyboardButton("Pay option updating",url = "https://t.me/fligher"),
        			InlineKeyboardButton("Pay option updating",url = "https://t.me/fligher")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 70  ind /🌎 1$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 150  ind /🌎 2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 225  ind /🌎 3$  per Month
	
	
	Pay Using ```Gpay,PhonePe,GooglePlayReedem```
	
	After Payment Send Screenshots Of 
        Payment To Admin @fligher"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/fligher")], 
        			[InlineKeyboardButton("Pay option updating",url = "https://t.me/fligher"),
        			InlineKeyboardButton("Pay option updating",url = "https://t.me/fligher")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
