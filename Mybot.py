import telebot
import mysql

import mytoken

from datetime import date
from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
from telebot import apihelper
waktusekarang=datetime.now()

class MyBot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):


        teks = mytoken.SAPA + "\n-- admin & developer @Rigel_iksandy - Love Liver -- "+\
               "\n hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)
    print("-- Bot sedang berjalan --")
    myBot.polling(none_stop=True)


