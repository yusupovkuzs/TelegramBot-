from telegram import KeyboardButton, ReplyKeyboardMarkup


def menu_keyboard():  # menu_buttons
    location_button = KeyboardButton('Отправить геопозицию \U0001F5FA', request_location=True)
    contact_button = KeyboardButton('Отправить контакты \U0001F4DE', request_contact=True)
    my_keyboard = ReplyKeyboardMarkup(
        [['Получить прикольчик \U0001F970'],
         [location_button, contact_button],
         ['Заполнить анкету \U0001F58A', 'Астрология \U0001F52E']],
        resize_keyboard=True)  # add buttons
    return my_keyboard


def back_to_menu():
    my_keyboard = ReplyKeyboardMarkup(
        [['Вернуться в меню \U0001F519']],
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return my_keyboard


def astrology_keyboard():
    my_keyboard = ReplyKeyboardMarkup(
        [['Мои данные \U0001F60E'],
         ['1-ый дом (ASC) \U0001F481', '10-й дом (MC) \U0001F4B8'],
         ['Планеты \U0001FA90', 'Объекты \U0001F30C'],
         ['Вернуться в меню \U0001F519']],
        resize_keyboard=True
    )
    return my_keyboard


def planet_keyboard():
    my_keyboard = ReplyKeyboardMarkup(
        [['Солнце \U00002600', 'Луна \U0001F311'],
         ['Меркурий\U0000263F ', 'Венера \U00002640'],
         ['Марс \U00002642', 'Юпитер \U00002643', 'Сатурн \U00002644'],
         ['Уран \U000026E2', 'Нептун \U00002646', 'Плутон \U00002647'],
         ['Вернуться обратно \U0001F52E']],
        resize_keyboard=True
    )
    return my_keyboard


def objects_keyboard():
    my_keyboard = ReplyKeyboardMarkup(
        [['Лунные узлы \U0001F31D'],
         ['Лилит \U000026B8', 'Хирон \U000026B7'],
         ['Вернуться обратно \U0001F52E']],
        resize_keyboard=True
    )
    return my_keyboard
