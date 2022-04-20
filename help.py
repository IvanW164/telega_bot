from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def help(update: Update, context: CallbackContext):    
    update.message.reply_text('Hello, my dear friend!\n Here are the commands that will help you to communicate with me')
    update.message.reply_text('You can send me a command /hello and I will greet you))')
    update.message.reply_text('Command /topic will start the game and guess a random word from three random categories: FRUITS, ANIMALS and CONTRIES')
    update.message.reply_text('to spell out a word use the command "/game (space) letter" (for example: you have to type "/game a" if you want to choose the letter a)')
    update.message.reply_text('Сhoose a command. And good luck!')