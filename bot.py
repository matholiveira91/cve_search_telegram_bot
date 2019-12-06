# AUTHOR MATHEUS OLIVEIRA
# LICENSE GPLV3 
# PURPUSE TELEGRAM BOT WHOS SEARCH TO CVE's by vendor or product

from telegram.ext import Updater,CommandHandler, MessageHandler, Filters 
import logging
from os import environ 
import procura_cve

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s',level-logging.INFO)
logger = logging.getLogger(_name_) 

#COMANDS

def start(bot,update):
    """Send a message when the command /start is issued."""
    full_name = update.message.from_user.full_name 
    message_start = (f"Boas vindas, {full_name}, ao bot CVE_search\n\n"
            "Comandos:\n\n /search vendor(or product) para procurar por cves\n\n /id to search byt CVE-ID  \n\n /last para exibir o ultimo registro disponível \n\n /help para exibir os comandos")
    update.message.reply_text

def help(bot, update):
    message.help = (
            " Comandos: " 
            "/search procura um produto especifico\n"
            "/id procura por uma CVE-ID\n"
            "/last mostra o ultimo registro disponível\n"
            "/help para exbir esta mensagem :sunglasses:\n"
            )
    update.message.reply_text(message_help)

def description(bot, update):
    message_description = ( 
            " Telegram bot para procurar por  CVE's, totalmente sotware livre \n"
            " Para saber mais sobre CVE's e sua definição visite: https://www.redhat.com/pt-br/topics/security/what-is-cve \n" 
            " Criticas e Pull Requests são bem-vindos, @0l1v3r2 para falar diretamente comigo :smile: ou visite nosso repositorio: https://github.com/matholiveira91/cve_search_telegram_bot \n" )
    update.message.reply_text(message_desciption)


            

