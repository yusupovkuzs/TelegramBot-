import random
from utils import get_keyboard
from settings import dic_comp, MY_UN
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode
from telegram.ext import ConversationHandler
from glob import glob


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text(
        '¡hola, preciosa! \U0001F970\ntienes un nombre bonito, {}, me gusta mucho!'.format(bot.message.chat.first_name),
        reply_markup=get_keyboard())
    print(bot.message)


def get_comp(bot, update):
    list_images = glob('images/love/*')
    picture = random.choice(list_images)
    comp = dic_comp[random.randint(1, 50)]
    pic_or_text = random.randint(0, 1)
    if pic_or_text == 0:
        bot.message.reply_text(comp)
    else:
        update.bot.send_photo(chat_id=bot.message.chat.id, photo=open(picture, 'rb'))


def get_contact(bot, update):
    print(bot.message.contact)
    bot.message.reply_text('{}, пользователь {} получил ваш контакт! \U0001F609'.format(bot.message.chat.first_name,
                                                                                        MY_UN))


def get_location(bot, update):
    print(bot.message.location)
    bot.message.reply_text('{}, пользователь {} получил вашу геопозицию! \U0001F609'.format(bot.message.chat.first_name,
                                                                                            MY_UN))


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def form_start(bot, update):
    bot.message.reply_text('Как тебя зовут? \U0001F60A', reply_markup=ReplyKeyboardRemove())
    return 'user_name'


def form_get_name(bot, update):
    update.user_data['name'] = bot.message.text
    bot.message.reply_text('Сколько тебе лет? \U0001F914')
    return 'user_age'


def form_get_age(bot, update):
    update.user_data['age'] = '' if bot.message.text == 'Пропустить' else bot.message.text
    reply_keyboard = [['Пропустить']]
    bot.message.reply_text('Твоя любимая группа? \U0001F3B5',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 'user_group'


def form_get_group(bot, update):
    update.user_data['group'] = '' if bot.message.text == 'Пропустить' else bot.message.text
    reply_keyboard = [['Пропустить']]
    bot.message.reply_text('Твой любимый фильм? \U0001F3AC',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 'user_film'


def form_get_film(bot, update):
    update.user_data['film'] = '' if bot.message.text == 'Пропустить' else bot.message.text
    reply_keyboard = [['Пропустить']]
    bot.message.reply_text('Твоя любимая еда? \U0001F60B',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 'user_eat'


def form_get_eat(bot, update):
    update.user_data['eat'] = '' if bot.message.text == 'Пропустить' else bot.message.text
    reply_keyboard = [['Пропустить']]
    bot.message.reply_text('Твоя любимая книга? \U0001F4DA',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 'user_book'


def form_get_book(bot, update):
    update.user_data['book'] = '' if bot.message.text == 'Пропустить' else bot.message.text
    reply_keyboard = [['Пропустить']]
    bot.message.reply_text('Твой любимый цвет? \U0001F308',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 'user_color'


def form_get_color(bot, update):
    update.user_data['color'] = '' if bot.message.text == 'Пропустить' else bot.message.text
    reply_keyboard = [['Пропустить']]
    bot.message.reply_text('Твоя мечта? \U0001F929',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 'user_dream'


def form_end(bot, update):
    update.user_data['dream'] = '' if bot.message.text == 'Пропустить' else bot.message.text
    text = ''' \U0001F60D Твоя анкета \U0001F60D:
    <i>\U0001F451 Имя \U0001F451:</i> <b> {name} </b> 
    <i>\U0001F92B Возраст \U0001F92B:</i> <b> {age} </b>
    <i>\U0001F3B8 Любимая группа \U0001F3B8:</i> <b> {group} </b>
    <i>\U0001F4FD Любимый фильм \U0001F4FD:</i> <b> {film} </b>
    <i>\U0001F37D Любимая еда \U0001F37D:</i> <b> {eat} </b>
    <i>\U0001F308 Любимый цвет \U0001F308:</i> <b> {color} </b>
    <i>\U0001F52E Мечта \U0001F52E:</i> <b> {dream} </b>
    '''.format(**update.user_data)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text('Спасибо за твои ответы!', reply_markup=get_keyboard())
    return ConversationHandler.END


def dont_know(bot, update):
    bot.message.reply_text('Я тебя не понимаю =(')
