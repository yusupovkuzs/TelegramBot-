import random
from utils import menu_keyboard, back_to_menu, astrology_keyboard, planet_keyboard, objects_keyboard
from settings import dic_comp, MY_UN, astrology_stickers
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode
from telegram.ext import ConversationHandler
from glob import glob


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text(
        '¡hola, preciosa! \U0001F970\n'
        'tienes un nombre bonito, {}, me gusta mucho! \U0001F63B'.format(bot.message.chat.first_name),
        reply_markup=menu_keyboard())
    print(bot.message)


def get_comp(bot, update):
    list_images = glob('images/love/*')
    picture = random.choice(list_images)
    comp = dic_comp[random.randint(1, 50)]
    pic_or_text = random.randint(0, 100)
    if pic_or_text >= 17:
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


# Анкета
def form_start(bot, update):
    list_images = glob('images/memes/form/*')
    picture = random.choice(list_images)
    update.bot.send_photo(chat_id=bot.message.chat.id, photo=open(picture, 'rb'))
    bot.message.reply_text('Как тебя зовут? \U0001F60A', reply_markup=back_to_menu())
    return 'user_name'


def form_get_name(bot, update):
    update.user_data['name'] = bot.message.text
    bot.message.reply_text('Сколько тебе лет? \U0001F914')
    return 'user_age'


def form_get_age(bot, update):
    update.user_data['age'] = '' if bot.message.text == 'Пропустить \U000023E9' else bot.message.text
    reply_keyboard = [['Пропустить \U000023E9']]
    bot.message.reply_text('Твоя любимая группа? \U0001F3B5',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))
    return 'user_group'


def form_get_group(bot, update):
    update.user_data['group'] = '' if bot.message.text == 'Пропустить \U000023E9' else bot.message.text
    reply_keyboard = [['Пропустить \U000023E9']]
    bot.message.reply_text('Твой любимый фильм? \U0001F3AC',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))
    return 'user_film'


def form_get_film(bot, update):
    update.user_data['film'] = '' if bot.message.text == 'Пропустить \U000023E9' else bot.message.text
    reply_keyboard = [['Пропустить  \U000023E9']]
    bot.message.reply_text('Твоя любимая еда? \U0001F60B',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))
    return 'user_eat'


def form_get_eat(bot, update):
    update.user_data['eat'] = '' if bot.message.text == 'Пропустить \U000023E9' else bot.message.text
    reply_keyboard = [['Пропустить  \U000023E9']]
    bot.message.reply_text('Твоя любимая книга? \U0001F4DA',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))
    return 'user_book'


def form_get_book(bot, update):
    update.user_data['book'] = '' if bot.message.text == 'Пропустить \U000023E9' else bot.message.text
    reply_keyboard = [['Пропустить  \U000023E9']]
    bot.message.reply_text('Твой любимый цвет? \U0001F308',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))
    return 'user_color'


def form_get_color(bot, update):
    update.user_data['color'] = '' if bot.message.text == 'Пропустить \U000023E9' else bot.message.text
    reply_keyboard = [['Пропустить  \U000023E9']]
    bot.message.reply_text('Твоя мечта? \U0001F929',
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True))
    return 'user_dream'


def form_end(bot, update):
    update.user_data['dream'] = '' if bot.message.text == 'Пропустить \U000023E9' else bot.message.text
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
    bot.message.reply_text('Спасибо за твои ответы!', reply_markup=menu_keyboard())
    return ConversationHandler.END


def dont_know(bot, update):
    bot.message.reply_text('Я тебя не понимаю =(')


def back(bot, update):
    bot.message.reply_text('Ты вернулась в меню \U0001F638', reply_markup=menu_keyboard())


def astrology_start(bot, update):
    list_images = glob('images/memes/astrology/*')
    picture = random.choice(list_images)
    sticker = random.choice(astrology_stickers)
    pic_ot_sticker = random.randint(0, 100)
    if pic_ot_sticker > 29:
        update.bot.send_photo(chat_id=bot.message.chat.id, photo=open(picture, 'rb'))
    else:
        update.bot.send_sticker(chat_id=bot.message.chat.id, sticker=sticker)
    _text = ''' Напиши мне, когда ты родилась \U0001F382
Дата в формате: <b>дд.мм.гггг</b>
<i>Пример: 09.05.2003</i>
    '''
    bot.message.reply_text(_text, parse_mode=ParseMode.HTML, reply_markup=back_to_menu())
    return 'user_birthday'


def astrology_time(bot, update):
    update.user_data['birthday'] = bot.message.text
    _text = ''' Если помнишь, то запиши время, в которое ты родилась \U0001F551
Время в формате: <b>чч:мм</b>
<i>Пример: 12:00</i>
    '''
    reply_keyboard = [['Не знаю  \U0001F937']]
    bot.message.reply_text(_text,
                           parse_mode=ParseMode.HTML,
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                            one_time_keyboard=True,
                                                            resize_keyboard=True))
    return 'user_bdtime'


def astrology_city(bot, update):
    update.user_data['bdtime'] = bot.message.text
    bot.message.reply_text('И наконец, я хочу узнать город, в котором появилось такое солнышко \U0001F3D9')
    return 'user_bdcity'


def astrology_end(bot, update):
    update.user_data['bdcity'] = bot.message.text
    text = '''<i>Что ты можешь узнать о себе? \U0001F50E</i>

<b>\U0001F60E --- Мои данные --- \U0001F60E</b>
Проверь, верно ли я запомнил все, что ты мне написала =) \U0000263A

<b>\U0001F481 --- 1-ый дом (ASC) --- \U0001F481</b>
Физическая оболочка
Асцендент (ASC) - Символизирует основные, базовые черты характера и личности, а также внешность,  темперамент, поведение, отношение к жизни, первое впечатление, которое человек производит.

<b>\U0001F4B8 --- 10-й дом (MC) --- \U0001F4B8</b>   
Карьера, престиж, репутация
Медиум Коели (Середина неба, MC) - Символизирует социальный статус, карьеру, репутацию, почести, славу, успех, авторитет, отца.

<b>\U0001FA90 --- Планеты --- \U0001FA90</b>
Солнце, Луна, Меркурий, Венера, Марс, Юпитер, Сатурн, Уран, Нептун, Плутон

<b>\U0001F30C --- Объекты --- \U0001F30C</b>
Лунные узлы, Лилит, Хирон
    '''
    bot.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=astrology_keyboard())


def astrology_menu(bot, update):
    text = '''<i>Что ты можешь узнать о себе? \U0001F50E</i>

<b>\U0001F60E --- Мои данные --- \U0001F60E</b>
Проверь, верно ли я запомнил все, что ты мне написала =) \U0000263A

<b>\U0001F481 --- 1ый дом (ASC) --- \U0001F481</b>
Физическая оболочка
Асцендент (ASC) - Символизирует основные, базовые черты характера и личности, а также внешность,  темперамент, поведение, отношение к жизни, первое впечатление, которое человек производит.

<b>\U0001F4B8 --- 10й дом (MC) --- \U0001F4B8</b>   
Карьера, престиж, репутация
Медиум Коели (Середина неба, MC) - Символизирует социальный статус, карьеру, репутацию, почести, славу, успех, авторитет, отца.

<b>\U0001FA90 --- Планеты --- \U0001FA90</b>
Солнце, Луна, Меркурий, Венера, Марс, Юпитер, Сатурн, Уран, Нептун, Плутон

<b>\U0001F30C --- Объекты --- \U0001F30C</b>
Лунные узлы, Лилит, Хирон
        '''
    bot.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=astrology_keyboard())


def astrology_planets(bot, update):
    text = '''<i>\U0001FA90 --- Планеты --- \U0001FA90</i>

<b>\U00002600 Солнце \U00002600</b>
Эго, индивидуальность, персона
<i>Солнце</i> символизирует самоидентификацию человека. Оно показывает то область, в которой мы должны быть независимы, где мы можем реализовать свой потенциал, подчеркнуть свою индивидуальность, сиять. Положение солнца может подсказать нам, какая профессия подойдет человеку.
    
<b>\U0001F311 Луна \U0001F311</b> 
Эмоции, инстинкты, корни, мать
<i>Положение луны</i> в гороскопе описывает то, в каких обстоятельствах мы чувствуем себя в безопасности, в комфорте. Показывает насколько мы чувствительны и как мы взаимодействуем с окружением на инстинктивном уровне. Луна также рассказывает о детстве и отношениях с матерью.
    
<b>\U0000263F Меркурий \U0000263F</b> 
Мышление, общение, интеллект, учёба
<i>Меркурий</i> - планета описывающая сферы интересов интеллектуальной деятельности, наш стиль обучения. Он показывает, насколько глубоко мы хотим изучать какие-либо темы, описывает тип интеллекта и способность воспринимать, анализировать и воспроизводить информацию. 
    
<b>\U00002640 Венера \U00002640</b>
Чувственность, любовь, гармония, удовольствия
<i>Венера</i> символизирует привлекательность. Знак, в котором находится Венера расскажет о том, что мы находим привлекательным, и то, что позволяет нам отдавать и получать любовь, симпатию, опишет наше представление о красоте и счастье, наши ценности. Негативной стороной Венеры является слабость и поверхностность. 
    
<b>\U00002642 Марс \U00002642</b>
Активность, энергия, смелость, настойчивость
<i>Марс</i> символизирует желание заполучить то что мы хотим. Это наша движущая сила, включая либидо, инициативу и смелость. Марс описывает наши желания, страсти, отвагу и силу воли. Также показывает, насколько мы способны преодолевать препятствия и насколько мы активны. 
    
<b>\U00002643 Юпитер \U00002643</b>
Счастье, оптимизм, расширение
<i>Юпитер</i> символизирует рост, расширение, законы, веру и этику, мораль. Показывает наше направление духовного роста, которое может привести к новым возможностям, удаче, богатству. Но если Юпитер повреждён, это может привести к аморальности и экстремизму. 
    
<b>\U00002644 Сатурн \U00002644</b>
Ограничение, порядок, зрелость, время
<i>Сатурн</i> - наш строгий учитель, который безжалостно тестирует нас на предмет зрелости. Но он не такой уж и деспот, он представляет собой архетип учителя, который использует боль, как способ привлечь наше внимание к проблеме, к слабому месту, над которым нужно работать. 
    
<b>\U000026E2 Уран \U000026E2</b>
Оригинальность, свобода, революция
<i>Уран</i> - это сила прозрения, которое зачастую ведёт к нарушению установленного порядка, к переменам. События под влиянием Урана непредсказуемы и неожиданны. Они заставляют нас идти по новому пути и смотреть в лицо правде касаемо того или иного вопроса. 
    
<b>\U00002646 Нептун \U00002646</b>
Фантазия, иллюзия, духовность, воображение
<i>Нептун</i> называют повелителем Невидимой Империи. Загадочное имя для загадочной планеты. Вероятно, мы можем описать это, как измерение, которое не познать пятью чувствами, мы можем его воспринять только через наше воображение. 
    
<b>\U00002647 Плутон \U00002647</b>
Трансформация, возрождение, власть
<i>Плутон</i> - планета смерти и перерождения. Это конец всего, Судный День. Он управляет одержимостью, навязчивыми идеями. В своих низших проявлениях он выражается как человек “во власти своих страстей”. Позитивное влияние Плутона создаёт человека, который способен докопаться до глубинной сути вещей, трансформировать негативную энергию в созидательную, принести исцеление.'''
    bot.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=planet_keyboard())


def astrology_objects(bot, update):
    text = '''<i>\U0001F30C --- Объекты --- \U0001F30C</i> 

<b>\U0001F31C Лунные узлы \U0001F31B</b>
Северный и Южный Узлы
<i>Лунные узлы</i> не являются физическими объектами. Они - точки пересечения лунной орбиты с плоскостью эклиптики и в натальной карте всегда находятся друг напротив друга. Считается, что цель воплощения заложена по оси узлов. Южный узел - зона комфорта, привычное место. Северный узел показывает уроки, которые предстоит освоить в этой жизни. Узлы движутся ретроградно. 

<b>\U000026B8 Лилит \U000026B8</b>
Черная луна - очарование и отрицание
<i>Лилит</i> - фиктивная точка на лунной орбите, находящаяся дальше всего от Земли. В мифологии Лилит отказалась слушаться Адама, восстала против подчинения ему и сбежала из Эдема, связавшись с Сатаной. В астрологии, Лилит символизирует либо одержимость, либо категорическую отстранённость от тем, описываемых её положением. Как одержимость, так и отрицание может полностью поглотить человека, заставив его нарушить связь с окружающим миром.

<b>\U000026B7 Хирон \U000026B7</b> 
Раненый Целитель, внутренний учитель
<i>Хирон</i> - это астероид между орбитами Сатурна и Урана. Его собственная орбита очень необычна и символизирует мост между материальным и духовным миром. В мифологии Хирон был великим целителем, мудрым учителем и одним из бессмертных Кентавров. Он был случайно ранен Гераклом, его любимым учеником, одной из стрел с ядом гидры. Поскольку он был бессмертен, он продолжал жить в страданиях от этой раны. В конце концов, он отдал свою бессмертность Прометею, который тоже страдал, а сам отправился в Аид - подземный мир. Там на него снизошла милость Зевса, который поместил его на небо. В астрологии Хирон символизирует наши незаживающие раны. Но если человек не зацикливается на них, а смиряется с болью и страданиями в жизни, и стремится помочь другим, тогда Хирон превращается в ключ к мудрости или даже указывает на “Путь к Инициации”.
    '''
    bot.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=objects_keyboard())


'''
    отправить запрос на сайт
    появляется astrology_keyboard
    --- actrology_keyboard ---
    > Мои данные:
        Дата рождения :               9 Мая 2003 - 12:00  (MSD, DST)
        Время по Гринвичу (UT/GMT):   9 Мая 2003 - 08:00  
        Звёздное время (LST):         02:35:09
        Система домов:                Placidus system
        Широта, Долгота:              55°19' с. ш., 52°4' в. д.
        Город рождения:               Zainsk
        Страна:                       Russia Russia (RU)
    > 1ый дом - Асцендент:
        (переходим на более)
        
        Асцендент в Льве
        Людям с асцендентом во Льве нужно использовать свою креативность, силу и авторитет. Они ищут любви, восхищения,
        аплодисментов. Некоторые могут быть эксцентричными и с силой проталкиваться в первые ряды. Они должны стараться
        стать независимыми и самобытными личностями. Потенциальная опасность для них - в гордыне. Чтобы заслужить 
        уважение и восхищение, им сначала нужно приложить усилия. Те, кто не смогут “засиять” могут стать озлобленными. 
        Переломным момент наступит тогда, когда они научатся давать, не ожидая чего-то взамен.

        Десцендент в Водолее
        Для лучших отношений, им нужно научится остужать свой огненный пыл и быть более объективными и справедливыми.
        Если у Вас Водолей на десценденте, нужно будет научится быть одним(одной) из многих. Немного ординарности 
        может сделать Вас более особенным(ой). Правитель, который относится ко всем подданным как к ровне, более 
        популярен, чем тот, который высокомерно держит дистанцию.
        
        Несмотря на непредсказуемость, в Ваших отношениях должен быть акцент на свободу. Может быть Вы выберете партнера
        с широкими взглядами, которые помогут Вам освободиться от тщеславия. 
    > 10й дом - Медиум Коели:
         
'''