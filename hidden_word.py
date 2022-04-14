import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hidden_word(update: Update, context: CallbackContext):
    list = ['cat','dog','pig']
    word = random.randint(0,len(list)+1)
    i=list[word]
    update.message.reply_text(f'{i}')
    # return list[word]
