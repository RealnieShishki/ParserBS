import telebot
from telebot import apihelper
import os
from main import news

TOKEN = '5590133073:AAFB5_XawZ-0YlmfU9VsIPHOQFbavLumKlY'

proxies = {
    'http': 'http://167.86.96.4:3128',
    'https': 'http://167.86.96.4:3128',
}

# apihelper.proxy = proxies

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, чего будем творить??")

@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'{text}!!!')

@bot.message_handler(commands=['news'])
def say(message):
    text = news()
    for i, j in text.items():
        bot.reply_to(message, f'{i, j}!!!')

@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.username == 'RealnieShishki':
        info = os.name
        bot.reply_to(message, info)
    else:
        bot.reply_to(message, 'Метод недоступен, нет прав')

@bot.message_handler(commands=['file'])
def get_file(message):
    with open('Володя.jpg', 'rb') as data:
        bot.send_photo(message.chat.id, data)


bot.polling()