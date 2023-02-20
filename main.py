import os

import dotenv
import openai
import telebot
from loguru import logger

from src import AskChatGPT

dotenv.load_dotenv()

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))
openai.api_key = os.environ.get('OPENAI_API_KEY')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info(message.__dict__["json"])
    bot.reply_to(message, "Olá, seja bem vindo! Eu sou o bot PiliP!")


@bot.message_handler(commands=['ask'])
def ask_openai(message):
    logger.info(message.__dict__["json"])

    bot.reply_to(message, 'Aguarde um momento...')

    try:
        ask_gtp = AskChatGPT(message.text)
        answer = ask_gtp.get_response_int_chat_gpt()
    except Exception as e:
        logger.error(e)
        answer = 'Desculpe... Houve um erro ao tentar processar sua pergunta.'

    bot.reply_to(message, answer)


logger.info('Bot started')
bot.infinity_polling()
