import telebot
from config import token
from random import choice

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я телеграм бот.Напиши /info чтобы узнать про бота и его команды.")

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, "Мой первый бот в телеграмме.\nКоманды: /fact - отправляет случайный факт.")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = choice(['Самая крупная жемчужина в мире достигает 6 килограммов в весе.',
        'Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.',
        'В Антарктиде существует единственная река – Оникс, она течет всего 60 дней в году.',
        'Лимон содержит больше сахара, чем клубника.',
        'У жирафа и человека одинаковое количество шейных позвонков.',
        'Корова может подняться по лестнице, но не может спуститься.',
        'Самая трудно излечимая фобия – боязнь страха.',
        'В мире всего 7% левшей',
        'На Юпитере регулярно идут алмазные дожди.']) 
    bot.reply_to(message, fact)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    
