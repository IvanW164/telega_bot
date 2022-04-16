from dataclasses import replace
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import re
from guess_word import word_competion


gamePlay = True

def hidden_word_topic(update: Update, context: CallbackContext):
    global censured_word
    whattopic = random.randint(1, 4)
    if whattopic == 1:
        update.message.reply_text('The topic is ANIMALS')
    elif whattopic == 2:
        update.message.reply_text('The topic is FRUITS')
    elif whattopic == 3:
        update.message.reply_text('The topic is CONTRIES')
    update.message.reply_text(f'{censured_word}, please enter /game (space) a letter you want to guess')
    return whattopic

def word_choise(whattopic):
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

word = word_choise(hidden_word_topic())
censured_word = re.sub('[a-z]','*',word)

def game(update: Update, context: CallbackContext):
    count = 8
    while gamePlay == True:
        msg = update.message.text
        reslist = msg.split()        
        if reslist[1] in word:
            word_user = word_competion(reslist[1], censured_word, word)
            censured_word = word_user
            if censured_word.find('*') != -1:
                update.message.reply_text(f'{censured_word}, please enter /game (space) a letter you want to guess')
            else:
                update.message.reply_text('Congratulations! You are win!')
                gamePlay = False
        else:
            update.message.reply_text(f'Your letter ({reslist[1]}) is NOT inside your word')
            count = count - 1
            if count == 7:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_142913.jpg?raw=true')
                break
            elif count == 6:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_142928.jpg?raw=true')
                break
            elif count == 5:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143033.jpg?raw=true')
                break
            elif count == 4:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143053.jpg?raw=true')
                break
            elif count == 3:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143123.jpg?raw=true')
                break
            elif count == 2:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143150.jpg?raw=true')
                break
            elif count == 1:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143211.jpg?raw=true')
                break
            elif count == 0:
                update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143224.jpg?raw=true')
                update.message.reply_text('You dont have more lifes, you are hanged')
                break

def again():
    global censured_word
    global gamePlay
    word = word_choise(hidden_word_topic())
    censured_word = re.sub('[a-z]','*',word)
    game()