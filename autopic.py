from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from PIL import Image, ImageDraw, ImageFont
import datetime
import asyncio
import random
import os

from . import *

dim = [(100, 200), (1280, 200), (1280, 1600), (100, 1600)]

wolfUB=Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

Time_Zone = os.environ["TIME_ZONE"]

async def main_shaka():
    try:
        while True:
            if wolfUB.is_connected:
    original = "resources/template.jpg"
    photo = "pic.png"
    shutil.copy(original, photo)
    current_time = datetime.now().strftime(
        f'%H:%M %d-%m-%y\nLife Is too short\nto argue.\njust say "fuck off"\nand move on.'
    )
    img = Image.open(photo)
    drawn_text = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("resources/Ubuntu-Title.ttf", 60)
    drawn_text.text(random.choice(dim), current_time, font=fnt, fill=(0, 0, 0))
    img.save(photo)
    file = await bot.upload_file(photo)
    try:
        d = await bot.get_profile_photos("me", limit=1)
        await bot(DeletePhotosRequest(d))
        await bot(UploadProfilePhotoRequest(file))
        os.remove(photo)
    except BaseException:
        return
      print("Profile Updated!")
            await asyncio.sleep(60)     
    except FloodWait as e:
        await asyncio.sleep(e.x)         

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_shaka())
wolfUB.run()
      
      
