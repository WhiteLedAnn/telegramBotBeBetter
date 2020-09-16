#!/usr/bin/env python3
#-*- coding: utf8 -*-
import sys
import telebot
from config import *


bot = telebot.TeleBot(TOKEN)


"""
print("Python ver", sys.version_info.major, sys.version_info.minor)
https://habr.com/ru/post/350648/
https://habr.com/ru/post/442800/
https://habr.com/ru/post/448310/
https://habr.com/ru/post/462905/
ttps://tproger.ru/translations/telegram-bot-create-and-deploy/
https://groosha.gitbook.io/telegram-bot-lessons/chapter1
https://momentum-bots.top/blog/2018/05/24/botheroku/
https://telegra.ph/Baza-dannyh-polzovatelej-Rassylki-04-21
"""

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доброго, ты написала мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока')

if __name__ == '__main__':
    bot.polling(none_stop=True)

#bywhiteled
