from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN, dic_comp, MY_UN
from telegram import ReplyKeyboardMarkup, KeyboardButton
import random
from bs4 import BeautifulSoup
import requests


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text(
        '¡hola, preciosa!\ntienes un nombre bonito, {}, me gusta mucho!'.format(bot.message.chat.first_name),
        reply_markup=get_keyboard())
    print(bot.message)


def get_comp(bot, update):
    rand_comp = random.randint(1, 50)
    bot.message.reply_text(dic_comp[rand_comp])


def get_contact(bot, update):
    print(bot.message.contact)
    bot.message.reply_text('Пользователь {} получил ваш контакт!'.format(MY_UN))


def get_location(bot, update):
    print(bot.message.location)
    bot.message.reply_text('Пользователь {} получил вашу геопозицию!'.format(MY_UN))


def get_keyboard():
    location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    my_keyboard = ReplyKeyboardMarkup(
        [['Получить прикольчик'], ['Начать'], [location_button, contact_button]], resize_keyboard=True)  # add buttons
    return my_keyboard


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def main():
    my_bot = Updater(TG_TOKEN)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Получить прикольчик'), get_comp))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, get_location))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()  # checks for the presence of messages from the Telegram
    my_bot.idle()  # the bot will work until it is stopped


main()
