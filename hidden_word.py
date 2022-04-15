import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

whattopic = random.randint(1, 4)

def hidden_word_topic(update: Update, context: CallbackContext):
    if whattopic == 1:
        update.message.reply_text('The topic is ANIMALS')
    elif whattopic == 2:
        update.message.reply_text('The topic is FRUITS')
    elif whattopic == 3:
        update.message.reply_text('The topic is CONTRIES')
   
def word():
    list1 = ['cat','dog','pig']
    list2 = ['apple', 'banana', 'orange']
    list3 = ['spain', 'france', 'germany']
    if whattopic == 1:
        i = random.randint(0, 2)
        word = list1[i]
        return word
    elif whattopic == 2:
        i = random.randint(0, 2)
        word = list2[i]
        return word
    elif whattopic == 3:
        i = random.randint(0, 2)
        word = list3[i]
        return word




