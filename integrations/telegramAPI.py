# BOT UserName: @MST_MST_BOT
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, dispatcher
import json
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

url = 'http://0.0.0.0:5005/webhooks/rest/webhook'


updater = Updater('5088250427:AAFBp7DXucNw2c7lPyQ28UgBUFratblWLr0')


def hello(update: Update, context: CallbackContext) -> None:
    print(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def echo(update: Update, context: CallbackContext):
    print(update, context)
    myobj = {'sender': 'raja', 'message': update.message.text}
    x = requests.post(url, json=myobj)
    jsonArray = json.loads(x.text)
    print(jsonArray)
    for i in jsonArray:
        key = "text"
        if 'image' in i:
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=i['image'])
        if 'text' in i:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=i['text'])


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")


# handler registrations
updater.dispatcher.add_handler(CommandHandler('hello', hello))
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
unknown_handler = MessageHandler(Filters.command, unknown)
updater.dispatcher.add_handler(echo_handler)
updater.dispatcher.add_handler(unknown_handler)


updater.start_polling()
updater.idle()
