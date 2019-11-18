# ATIHOR MATHEUS OLIVEIRA
# LICENSE GPLV3 
# PURPUSE TELEGRAM BOT WHOS SEARCH TO CVE's by vendor or product

from telegram.ext import Updater,CommandHandler, MessageHandler, Filters 
import logging
from os import environ 


logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s',level-logging.INFO)
logger = logging.getLogger(_name_) 

#COMANDS

def start(bot,update):
    """Send a message when the command /start is issued."""
    full_name = update.message.from_user.full_name 
    message_start = (f"Boas vindas, {full_name}, ao bot CVE_search\n\n"
            "Comandos:\n\n /search vendor(or product) para procurar por cves\n\n /limit: define o limite de cves do retorno \n\n /help para exibir os comandos")
    

