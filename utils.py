from telegram import  KeyboardButton, ReplyKeyboardMarkup


def get_keyboard():  # menu_buttons
    location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    my_keyboard = ReplyKeyboardMarkup(
        [['Получить прикольчик'], ['Начать'], [location_button, contact_button]], resize_keyboard=True)  # add buttons
    return my_keyboard