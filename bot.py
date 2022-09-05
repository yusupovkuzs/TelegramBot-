from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN
from handlers import sms, get_comp, get_contact, get_location, parrot


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


if __name__ == '__main__':
    main()
