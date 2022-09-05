import random
from utils import get_keyboard
from settings import dic_comp, MY_UN


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


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)