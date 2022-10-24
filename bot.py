from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN
from handlers import *
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def main():
    my_bot = Updater(TG_TOKEN)
    logging.info('Start bot')

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Получить прикольчик \U0001F970'), get_comp))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Вернуться в меню \U0001F519'), back))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Вернуться обратно \U0001F52E'), astrology_menu))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Планеты'), astrology_planets))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Объекты'), astrology_objects))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, get_location))

    # анкета
    my_bot.dispatcher.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Заполнить анкету \U0001F58A'), form_start)],
                            states={
                                'user_name': [MessageHandler(Filters.text, form_get_name)],
                                'user_age': [MessageHandler(Filters.text, form_get_age)],
                                'user_group': [MessageHandler(Filters.regex('Пропустить \U000023E9'), form_get_group),
                                               MessageHandler(Filters.text, form_get_group)],
                                'user_film': [MessageHandler(Filters.regex('Пропустить \U000023E9'), form_get_film),
                                              MessageHandler(Filters.text, form_get_film)],
                                'user_eat': [MessageHandler(Filters.regex('Пропустить \U000023E9'), form_get_eat),
                                             MessageHandler(Filters.text, form_get_eat)],
                                'user_book': [MessageHandler(Filters.regex('Пропустить \U000023E9'), form_get_book),
                                              MessageHandler(Filters.text, form_get_book)],
                                'user_color': [MessageHandler(Filters.regex('Пропустить \U000023E9'), form_get_color),
                                               MessageHandler(Filters.text, form_get_color)],
                                'user_dream': [MessageHandler(Filters.regex('Пропустить \U000023E9'), form_end),
                                               MessageHandler(Filters.text, form_end)]
                            },
                            fallbacks=[MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document,
                                                      dont_know)]
                            )
    )
    # astrology
    my_bot.dispatcher.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Астрология \U0001F52E'), astrology_start)],
                            states={
                                'user_birthday': [MessageHandler(Filters.text, astrology_time)],
                                'user_bdtime': [MessageHandler(Filters.regex('Не знаю \U0001F937'), astrology_city),
                                                MessageHandler(Filters.text, astrology_city)],
                                'user_bdcity': [MessageHandler(Filters.text, astrology_end)]
                            },
                            fallbacks=[MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document,
                                                      dont_know)]
                            )
    )

    my_bot.start_polling()  # checks for the presence of messages from the Telegram
    my_bot.idle()  # the bot will work until it is stopped


if __name__ == '__main__':
    main()
