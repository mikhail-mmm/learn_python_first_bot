import logging
import ephem
import datetime as dt
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='learn_bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    print(update)
    update.message.reply_text('Привет!')

def planet_info(update, context):
    print('Вызван /planet')
    print(update)
    user_message = update.message.text.split()
    print(user_message)
    print(user_message[1])
    today_date = dt.datetime.today().strftime('%Y/%m/%d')
    print(today_date)
    if user_message[1].lower() == 'mercury':
        mercury = ephem.Mercury(today_date)
        constellation = ephem.constellation(mercury)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    elif user_message[1].lower() == 'venus':
        venus = ephem.Venus(today_date)
        constellation = ephem.constellation(venus)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    elif user_message[1].lower() == 'earth':
        earth = ephem.Earth(today_date)
        constellation = ephem.constellation(earth)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    elif user_message[1].lower() == 'mars':
        mars = ephem.Mars(today_date)
        constellation = ephem.constellation(mars)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    elif user_message[1].lower() == 'jupiter':
        jupiter = ephem.Jupiter(today_date)
        constellation = ephem.constellation(jupiter)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    elif user_message[1].lower() == 'saturn':
        saturn = ephem.Saturn(today_date)
        constellation = ephem.constellation(saturn)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    elif user_message[1].lower() == 'uranus':
        uranus = ephem.Uranus(today_date)
        constellation = ephem.constellation(uranus)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    elif user_message[1].lower() == 'neptune':
        neptune = ephem.Neptune(today_date)
        constellation = ephem.constellation(neptune)
        print(constellation)
        update.message.reply_text(' '.join(constellation))
    else:
        update.message.reply_text('Такой планеты нет в списке.')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Запуск бота.')

    mybot.start_polling()

    mybot.idle()
    
if __name__ == 'main':
    main()
