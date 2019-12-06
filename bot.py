# AUTHOR MATHEUS OLIVEIRA
# LICENSE GPLV3 
# PURPUSE TELEGRAM BOT WHOS SEARCH TO CVE's by vendor or product

from telegram.ext import Updater, CommandHandler, MessageHandler 
import logging
from os import environ 
from procura_cve import busca_produto

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Commands
def search(bot, update):
   text = " ".join(update["message"]["text"].split()[1:])
   # Chamar funcao
   blob = busca_produto(text)
   message_search = (
           f"Pesquisa: {blob}\n"
           "Resultado:"
           )
   update.message.reply_text(message_search)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

# Motor
def main():
    """Start the bot."""
    updater = Updater(environ["TOKEN"])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("search", search))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

            

