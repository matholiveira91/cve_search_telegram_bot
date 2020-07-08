# AUTHOR MATHEUS OLIVEIRA
# LICENSE GPLV3 
# PURPUSE TELEGRAM BOT WHOS SEARCH TO CVE's by vendor or product

from telegram.ext import Updater, CommandHandler, MessageHandler 
from dotenv import load_dotenv
from os import environ
from support import cve
load_dotenv()

def term(bot, update):
   text = " ".join(update["message"]["text"].split()[1:])
   blob = cve.get_data(text)
   message_search = (
           f"{cve.result(blob)}"
           )
   update.message.reply_text(message_search)

def cvid(bot, update):
   text = " ".join(update["message"]["text"].split()[1:])
   blob = cve.search_cvid(text)
   message_search = (
           f"{cve.result(blob)}"
           )
   update.message.reply_text(message_search)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    print(f"[{update}] Erro: {error}")

if __name__ == '__main__':
    """Start the bot."""
    updater = Updater(environ["TOKEN"])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("term", term))
    dp.add_handler(CommandHandler("cvid", cvid))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

