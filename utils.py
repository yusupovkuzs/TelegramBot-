from telegram import KeyboardButton, ReplyKeyboardMarkup


def get_keyboard():  # menu_buttons
    location_button = KeyboardButton('Отправить геопозицию \U0001F5FA', request_location=True)
    contact_button = KeyboardButton('Отправить контакты \U0001F4DE', request_contact=True)
    my_keyboard = ReplyKeyboardMarkup(
        [['Начать'],
         ['Получить прикольчик \U0001F970'],
         [location_button, contact_button],
         ['Заполнить анкету \U0001F58A']],
        resize_keyboard=True)  # add buttons
    return my_keyboard
