#Import libraries
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from like_db import LikeDB

#Import TOKEN from envoirment variable
import os
TOKEN = "5699418530:AAF-rw_GFSO_DeL-19T4s2eiGDXLk6OSTIg" #os.environ['TOKEN']

#Create start command handler
def start(update:Update, context:CallbackContext):
    """Starts with picture all likes and all dislikes"""
    data = LikeDB('like_db.json')
    like = data.all_likes()
    liked = data.all_dislikes()

    text = f'like and dislike'
    inlineKeyboard = InlineKeyboardButton(f'👎{liked}',callback_data='dislike')
    inlineKeyboard1 = InlineKeyboardButton(f'👍{like}',callback_data='like')
    reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
    update.message.reply_text(text, reply_markup=reply_markup)

def like(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    query = update.callback_query
    user_id = query.from_user.id

    data = LikeDB('like_db.json')
    data.add_like(str(user_id))

    like = data.all_likes()
    liked = data.all_dislikes()

    text = f'like and dislike'
    inlineKeyboard = InlineKeyboardButton(f'👎{liked}',callback_data='dislike')
    inlineKeyboard1 = InlineKeyboardButton(f'👍{like}',callback_data='like')
    reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
    query.edit_message_text(text, reply_markup=reply_markup)

def dislike(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    query = update.callback_query
    user_id = query.from_user.id

    data = LikeDB('like_db.json')
    data.add_dislike(str(user_id))

    like = data.all_likes()
    liked = data.all_dislikes()

    text = f'like and dislike'
    inlineKeyboard = InlineKeyboardButton(f'👎{liked}',callback_data='dislike')
    inlineKeyboard1 = InlineKeyboardButton(f'👍{like}',callback_data='like')
    reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
    query.edit_message_text(text, reply_markup=reply_markup)

#Create updater and dispatcher
updater = Updater(TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(like, pattern='like'))
updater.dispatcher.add_handler(CallbackQueryHandler(dislike, pattern='dislike'))

#Start the bot
updater.start_polling()
updater.idle()