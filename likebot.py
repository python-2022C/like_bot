#Import libraries
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from like_db import LikeDB

#Import TOKEN from envoirment variable
import os
TOKEN = os.environ['TOKEN']

#Create start command handler
def start(update:Update, context:CallbackContext):
    """Starts with picture all likes and all dislikes"""
    data = LikeDB('like_db.json')
    like = data.all_likes()
    liked = data.all_dislikes()
    user_id = str(update.message.from_user.id)
    dat_db = data.db
    data.add_user(user_id=user_id)
    user_like = dat_db[user_id]['like']
    user_dislike = dat_db[user_id]['dislike']

    inlineKeyboard = InlineKeyboardButton(f'👎{liked}',callback_data='dislike')
    inlineKeyboard1 = InlineKeyboardButton(f'👍{like}',callback_data='like')
    reply_markup = InlineKeyboardMarkup([[inlineKeyboard1, inlineKeyboard]])
    update.message.reply_photo( 'https://www.drupal.org/files/project-images/like_and_dislike.png',reply_markup=reply_markup, caption=f'You have {user_like} likes and {user_dislike} dislikes')

def like(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    query = update.callback_query
    user_id = query.from_user.id

    data = LikeDB('like_db.json')
    data.add_like(str(user_id))
    user_id2 = str(query.from_user.id)
    dat_db = data.db
    user_like = dat_db[user_id2]['like']
    user_dislike = dat_db[user_id2]['dislike']

    like = data.all_likes()
    liked = data.all_dislikes()

    inlineKeyboard = InlineKeyboardButton(f'👎{liked}',callback_data='dislike')
    inlineKeyboard1 = InlineKeyboardButton(f'👍{like}',callback_data='like')
    reply_markup = InlineKeyboardMarkup([[inlineKeyboard1,inlineKeyboard]])
    query.edit_message_caption(reply_markup=reply_markup, caption=f'You have {user_like} likes and {user_dislike} dislikes')

def dislike(update:Update, context:CallbackContext):
    """Send the message with the number of likes and dislikes"""
    query = update.callback_query
    user_id = query.from_user.id

    data = LikeDB('like_db.json')
    data.add_dislike(str(user_id))
    user_id2 = str(query.from_user.id)
    dat_db = data.db
    user_like = dat_db[user_id2]['like']
    user_dislike = dat_db[user_id2]['dislike']

    like = data.all_likes()
    liked = data.all_dislikes()

    inlineKeyboard = InlineKeyboardButton(f'👎{liked}',callback_data='dislike')
    inlineKeyboard1 = InlineKeyboardButton(f'👍{like}',callback_data='like')
    reply_markup = InlineKeyboardMarkup([[inlineKeyboard1,inlineKeyboard]])
    query.edit_message_caption(reply_markup=reply_markup, caption=f'You have {user_like} likes and {user_dislike} dislikes')

#Create updater and dispatcher
updater = Updater(TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(like, pattern='like'))
updater.dispatcher.add_handler(CallbackQueryHandler(dislike, pattern='dislike'))

#Start the bot
updater.start_polling()
updater.idle()