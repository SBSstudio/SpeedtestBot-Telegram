# © BugHunterCodeLabs ™
# © bughunter0 / nuhman_pk
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os 
from os import error
import speedtest   
import logging
import pyrogram
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message

    
bughunter0 = Client(
    "SpeedTestBot",
    bot_token = os.environ["1989867894:AAHUn3lP84k4iS-VGIeU3FLetRXIIEo9OBs"],
    api_id = int(os.environ["3283847"]),
    api_hash = os.environ["432c6eebf8df924b27be598c295c3692"]
)


def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "https://telegra.ph/file/3f81561e07a2fcaadbf26.jpg",
    "caption": "Get instant access to Corona in Sri Lanka 📊 .  Automatically retrieve the latest corona information after adding it to the @SLCovid19slbzonebot Group 🦠 . Use /help for more information. @sl_bot_zone ",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": " 💎 Youtube  ",
                    "url": "https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA"
                }, 
                {
                    "text": " 🔔 ",
                    "callback_data": "/help"
                }
            ]
        ]
    }
}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, callback_data, data=json.dumps(data), headers=headers)

    
@bughunter0.on_message(filters.command(["go"]))
async def download_upload(bot, message):
     alert = await message.reply_text("Processing . . .")
     speed = speedtest.Speedtest() 
     await alert.edit("Connecting to server . . .")
     speed.get_best_server()
     await alert.edit(f'**Connected to :** {speed.results.server["sponsor"]} ({speed.results.server["name"]})')
     message = await message.reply_text("Checking Speed . . .")
     downloadspeed = speed.download()
     downloadspeed = downloadspeed/1000000 # bit to kbps
     uploadspeed = speed.upload()
     uploadspeed = uploadspeed/1000000 # bit to kbps
     await alert.delete()
     await message.edit_text(f' ꜱ̶ᴘ̶ᴇ̶ᴇ̶ᴅ̶ ̶ᴛ̶ᴇ̶ꜱ̶ᴛ̶ ̶ʀ̶ᴇ̶ꜱ̶ᴜ̶ʟ̶ᴛ̶  \n\n**●Download Speed :** `{downloadspeed} kbps` \n**●Upload Speed :** `{uploadspeed} kbps` \n**●Server :** {speed.results.server["sponsor"]} ({speed.results.server["name"]})\n\n ©️ @TGspeedtestBot|@SBS_Studio')

    
@bughunter0.on(events.NewMessage(pattern='/start'))
async def start(event):
    staat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation
    
bughunter0.run()
