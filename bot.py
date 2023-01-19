import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5793472760:AAE2N3-RFo0V-8S87fke4iCROCWjRS3kWrc")

API_ID = int(os.environ.get("API_ID", "16533237"))

API_HASH = os.environ.get("API_HASH", "384ffd14566ba610992d5561e0c553e6")

STRING = os.environ.get("STRING", "BQFcl6gAYxKbku5ndjPjd6ajLigSnpLQdgR3OXyhytgaZa7UxYkfZG9Sy8XBAmXiPuojx_YnpcSiBsWpvFKD28DyM3dcsDCAsv8Y71Vr8PKa38-GGsiBZHt_tCnAKLdUGUUTqWFAEZhgtTCnrtEqRaE6yuvYY0PycoAcIFRMMNvBr4arfx3rruZuOn9fb6crAkJkeXP303cQNklDheitAKj-7FDU8xa9tj07r5X6RfA_vc72i6XfVJFgmX5xui6SylvF696MRJbSEzGW2sOVBPxL5dNdfTUz-nN2qrRPSP703UFmE1s8la2XSgcsdr5tZw6V0em-uh5kzcYW8cP9bSwToNaPiwAAAAFkK0eEAA")

PORT = os.environ.get("PORT","8080")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
