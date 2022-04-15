from dataclasses import replace
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import hidden_word as hd
import re


word = hd.word()
censured_word = re.sub('[a-z]','*',word)
count = 8

def game(update: Update, context: CallbackContext):
    global count
    while True:
        update.message.reply_text(f'This is the word you should guess {censured_word}, please enter /game (space) a letter you want to guess')
        msg = update.message.text
        reslist = msg.split()
        if reslist[1] in word:
            update.message.reply_text(f'Your letter ({reslist[1]}) is inside the word')
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



    