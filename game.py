from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import re
import guess_word as gw
import hidden_word as hd


whattopic = random.randint(1, 4)
word = hd.choise_hidden_word(whattopic)
censured_word = re.sub('[a-z]','*', word)
# censured_word = hd.replace_word(word)

def choise_topic(update: Update, context: CallbackContext):
    list_topics = ['ANIMALS','FRUITS','COUNTRIES']
    if whattopic == 1:
        update.message.reply_text(f'The topic is {list_topics[whattopic-1]}')
    elif whattopic == 2:
        update.message.reply_text(f'The topic is {list_topics[whattopic-1]}')
    elif whattopic == 3:
        update.message.reply_text(f'The topic is {list_topics[whattopic-1]}')
    return update.message.reply_text(f'{censured_word}, please enter /game (space) a letter you want to guess')

count = 8
alphabet = gw.alphabet_method()

def game(update: Update, context: CallbackContext):
    global word
    global censured_word
    msg = update.message.text
    reslist = msg.lower().split()
    if reslist == ["/game"]:
        update.message.reply_text('Please! Enter one letter!')
    elif reslist[1] == word:
        update.message.reply_text('Congratulations! You are win!')
    elif len(reslist[1]) > 1 and reslist[1] != word:
        update.message.reply_text('Please! Enter one letter!')
    elif reslist[1] not in alphabet:
        update.message.reply_text('Please! Enter one english letter!')
    else:
        while True:
            if reslist[1] in word:
                word_user = gw.word_competion(reslist[1], censured_word, word)
                censured_word = word_user
                if censured_word.find('*') != -1:
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                else:
                    update.message.reply_text(f'{censured_word}\nCongratulations! You are win!')
                break
            else:
                update.message.reply_text(f'Your letter ({reslist[1]}) is NOT inside hidden word')
                count = count - 1
                if count == 7:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_142913.jpg?raw=true')
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                    break
                elif count == 6:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_142928.jpg?raw=true')
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                    break
                elif count == 5:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143033.jpg?raw=true')
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                    break
                elif count == 4:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143053.jpg?raw=true')
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                    break
                elif count == 3:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143123.jpg?raw=true')
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                    break
                elif count == 2:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143150.jpg?raw=true')
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                    break
                elif count == 1:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143211.jpg?raw=true')
                    update.message.reply_text(f'{censured_word}, please, enter /game (space) a letter you want to guess')
                    break
                elif count == 0:
                    update.message.reply_photo('https://github.com/Blakyyy/telega_bot/blob/main/20220415_143224.jpg?raw=true')
                    update.message.reply_text('You dont have more lifes, you are hanged! HAHAHA!')
                    break
