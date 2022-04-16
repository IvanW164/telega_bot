from dataclasses import replace
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
from guess_word import word_competion
import hidden_word as hd


def game(update: Update, context: CallbackContext):
    word, censured_word, whattopic = hd.choise_hidden_word(number_topic)
    del whattopic
    count = 8
    while True:
        msg = update.message.text
        reslist = msg.split()       
        if reslist[1] in word:
            word_user = word_competion(reslist[1], censured_word, word)
            censured_word = word_user
            if censured_word.find('*') != -1:
                update.message.reply_text(f'{censured_word}, please enter /game (space) a letter you want to guess')
            else:
                update.message.reply_text('Congratulations! You are win!')
            break
        else:
            update.message.reply_text(f'Your letter ({reslist[1]}) is NOT inside your word')
            update.message.reply_text(f'{censured_word}, please enter /game (space) a letter you want to guess')
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

def again(update: Update, context: CallbackContext):
    update.message.reply_text('Okay, please enter /topic')
    game()