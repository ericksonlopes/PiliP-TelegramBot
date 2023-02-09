import os

import dotenv
import openai
import telebot
from loguru import logger

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

    ask = message.text.replace('/ask ', '')

    bot.reply_to(message, 'Aguarde um momento...')

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=ask,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )

    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'Desculpe... Houve um erro ao tentar processar sua pergunta.')

    else:
        answer: str = response['choices'][0]['text'].replace('\n', ' ')

        logger.info("Question: {ask} - Answer: {text}".format(ask=ask, text=answer))
        bot.reply_to(message, answer)


logger.info('Bot started')
bot.infinity_polling()
