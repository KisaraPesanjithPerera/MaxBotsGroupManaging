from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from EMIlia import bot
from pyrogram import filters 
from EMIlia.plugins.stats import col
from EMIlia.plugins.stats import users_db , grps
from EMIlia import help_message


@bot.on_message(filters.command('start'))
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
            
    except Exception as e:
        bot.send_message(-1001664540730  , f"error in adding stats:\n\n{e}")
        
   
    
    if message.chat.type == "private" and not "help" in message.text:

        bot.send_sticker("CAACAgIAAxkBAAIDHmFiw6B43Xm-h7Z3YB9Rxn13r3HbAAIdAAOymJoOCsdwJVjxY24eBA")
    if "help" in message.text:
     bot.send_sticker("CAACAgIAAxkBAAIDHmFiw6B43Xm-h7Z3YB9Rxn13r3HbAAIdAAOymJoOCsdwJVjxY24eBA")
    if not message.chat.type == "private":
         message.reply("Hello")
