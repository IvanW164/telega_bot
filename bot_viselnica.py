from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import hidden_word as hd
import game as gm
import help


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5311753371:AAE_hvFU2BT3XtKv5yvuMj45bZULxT8u0kc')


updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('topic', gm.choice_topic))
updater.dispatcher.add_handler(CommandHandler('game', gm.game))
updater.dispatcher.add_handler(CommandHandler('help', help.help))

print('server_started')

updater.start_polling()
updater.idle()