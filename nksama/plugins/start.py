from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters 
from nksama.plugins.stats import col
from nksama.plugins.stats import users_db , grps
from nksama import help_message



@bot.on_message(filters.command('start') | filters.command('start@MHOFilter_bot'))
def start(_,message):
    try:
        if message.chat.type == "private":
            users = col.find({})
            mfs = []
            for x in users:
                mfs.append(x['user_id'])
            if message.from_user.id not in mfs:
                user = {"type": "user" , "user_id": message.from_user.id}
                col.insert_one(user)
                
        else:
            users = grps.find({})
            mfs = []
            for x in users:
                mfs.append(x['chat_id'])
            if message.chat.id not in mfs:
                grp = {"type": "group" , "chat_id": message.chat.id}
                grps.insert_one(grp)
