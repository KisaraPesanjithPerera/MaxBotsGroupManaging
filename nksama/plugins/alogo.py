from pyrogram import Client as bot
from pyrogram import filters
import os 
from PIL import Image, ImageDraw, ImageFont
import random

fontpath = "./resources/fonts/"
listfonts = os.listdir(fontpath)
fillcolour = ["blue", 
          "red", 
          "green"
          "yellow"]
outcolour = ["yellow", 
            "blue", 
            "green"
            "red",]
imgpath ="./resources/images/"
listano = os.listdir(imgpath + "anonymous")

@bot.on_message(filters.command("hlogo"))
async def logomake(_, message):
    if len(message.command) < 2:
            return await message.reply_text("Please give a text to make your logo 🤗")
    m = await message.reply_text("Creating your Logo 🚀")
    text = message.text.split(None, 1)[1]
    img = Image.open(imgpath + "anonymous/" + (random.choice(listano)))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    font = ImageFont.truetype(fontpath + (random.choice(listfonts)),150)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill=(random.choice(fillcolour)), stroke_width=2, stroke_fill=(random.choice(outcolour)))
    anlogo = "anlogo.png"
    img.save(anlogo, "png")
    await message.reply_photo(
                photo=f"anlogo.png",
                caption="Your logo was created By @MovieHubOfficialSL",
            )
    await m.delete()       
    if os.path.exists(anlogo):
            os.remove(anlogo)
