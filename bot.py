from time import sleep
from datetime import date, datetime
import schedule as schedule
import telebot
from itertools import islice
import configparser

config = configparser.ConfigParser()
config.read("setting.ini")

TOKEN = config.get('Telegram', 'TOKEN')
INSTANT_VIEW_ID = config.get('Telegram', 'INSTANT_VIEW_ID')
CHANNEL_ID = int(config.get('Telegram', 'CHANNEL_ID'))
ADMIN_ID = int(config.get('Telegram', 'ADMIN_ID'))

YEAR = int(config.get('Date', 'YEAR'))
MONTH = int(config.get('Date', 'MONTH'))
DAY = int(config.get('Date', 'DAY'))

bot = telebot.TeleBot(TOKEN)


# import logging
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)


def genlink(link, name):
    return f"<a href='{link}'>{name}</a>"


def ins_view(link):
    return f"https://t.me/iv?url={link}&rhash={INSTANT_VIEW_ID}"


def s_in_file(n, filename):
    lines = islice(open(filename), n - 1, n)
    for g in lines:
        return g


def diff_dates(date1, date2):
    return abs(date2 - date1).days


def delta_date(year, month, day):
    d1 = date(year, month, day)
    d2 = date(YEAR, MONTH, DAY)
    result1 = diff_dates(d2, d1)
    return result1


@bot.channel_post_handler()
def to_submit():
    now = datetime.now()
    count = delta_date(now.year, now.month, now.day)
    link = s_in_file(count, "articles1.txt")
    name = s_in_file(count, "names1.txt")
    bot.send_message(CHANNEL_ID, genlink(ins_view(link), name), parse_mode="html")
    bot.send_message(ADMIN_ID, count)


if __name__ == '__main__':
    schedule.every().day.at("15:00").do(to_submit)
    while True:
        schedule.run_pending()
        sleep(1)
bot.polling(none_stop=True, interval=0)
