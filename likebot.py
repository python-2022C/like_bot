#Import libraries
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from like_db import LikeDB

#Import TOKEN from envoirment variable
import os
TOKEN = os.environ['TOKEN']

liked= 0
disliked = 0

#Create start command handler
def start(update:Update, context:CallbackContext):
    
    photo = "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg"
    inlineKeyboard1 = InlineKeyboardButton(f"👍{liked}", callback_data='like')
    inlineKeyboard2 = InlineKeyboardButton(f"👎{disliked}", callback_data='dislike')
    reply_markup = InlineKeyboardMarkup([[inlineKeyboard1, inlineKeyboard2]])
    update.message.reply_photo(photo, reply_markup=reply_markup)
    return

def like(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    pass
def dislike(update:Update, context:CallbackContext):
    pass
#Create updater and dispatcher
updater = Updater(TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(like, pattern='like'))
updater.dispatcher.add_handler(CallbackQueryHandler(dislike, pattern='dislike'))

#Start the bot
updater.start_polling()
updater.idle()



