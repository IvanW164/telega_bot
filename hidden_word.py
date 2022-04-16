from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import re


def replace_word(some_word):
    res_word = ""
    for i in range(len(some_word)):
        res_word = res_word + "*"
    # res_word = re.sub('[a-z]','*',some_word)
    return res_word

# def rand_topic():
#     number_topic = random.randint(1, 4)
#     return number_topic

def choise_hidden_word(whattopic):
    list1 = ['cat','dog','pig']
    list2 = ['apple', 'banana', 'orange']
    list3 = ['spain', 'france', 'germany']
    if whattopic == 1:
        i = random.randint(0, 3)
        word = list1[i]
    elif whattopic == 2:
        i = random.randint(0, 3)
        word = list2[i]
    elif whattopic == 3:
        i = random.randint(0, 3)
        word = list3[i]
    censured_word = replace_word(word)
    return word, censured_word, whattopic

def choise_topic(update: Update, context: CallbackContext):
    number_topic = random.randint(1, 4)
    word, censured_word, whattopic = choise_hidden_word(number_topic)
    del word
    list_topics = ['ANIMALS','FRUITS','COUNTRIES']
    if whattopic == 1:
        update.message.reply_text(f'The topic is {list_topics[whattopic-1]}')
    elif whattopic == 2:
        update.message.reply_text(f'The topic is {list_topics[whattopic-1]}')
    elif whattopic == 3:
        update.message.reply_text(f'The topic is {list_topics[whattopic-1]}')
    return update.message.reply_text(f'{censured_word}, please enter /game (space) a letter you want to guess')

print(replace_word("ololosh"))