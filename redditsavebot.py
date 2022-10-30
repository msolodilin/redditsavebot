import telebot
import praw
import requests
from RedDownloader import RedDownloader
import datetime
import time
import schedule
import os


def video_checker(url_input):
    try:
        get = requests.get(url_input)
        if get.status_code == 200:
            submission = reddit.submission(url=url_input)
            return submission.is_video
        else:
            return f'{url_input}: does not seem to be a valid URL, status_code: {get.status_code}'
    except requests.exceptions.RequestException as exc:
        return exc


def photo_downloader(url_input):
    submission = reddit.submission(url=url_input)
    return submission.url


def clean_old_files():
    for i in os.listdir(file_path):
        path = os.path.join(file_path, i)

        if os.stat(path).st_mtime <= time.time() - 86400:
            try:
                os.remove(path)
                print('Old files deleted, check again tomorrow!')
            except i:
                return 'Could not remove file:', i


token = 'telegram bot token'
bot = telebot.TeleBot(token)

reddit = praw.Reddit(client_id='your client id',
                     client_secret='your client secret',
                     user_agent='your user agent')

reddit_regex = r'^http(?:s)?://(?:www\.)?(?:[\w-]+?\.)?reddit.com(/r/|/user/)?(?(1)([\w:]{2,21}))(/comments/)?' \
               r'(?(3)(\w{5,6})(?:/[\w%\\\\-]+)?)?(?(4)/(\w{7}))?/?(\?)?(?(6)(\S+))?(\#)?(?(8)(\S+))?$'


@bot.message_handler(regexp=reddit_regex)
def main_action(message):
    message_id = message.id
    url = message.text
    if video_checker(url):
        message_unix = message.date
        message_time = datetime.datetime.fromtimestamp(int(message_unix))
        file_name = 'vid_' + str(message_unix)
        bot.send_message(message.chat.id, 'Downloading video from ' + str(message_time) +
                         '. This will only take a minute! ✌')
        RedDownloader.Download(url, output=file_name, destination='./saved_videos/')
        video = open(f'./saved_videos/{file_name}.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        bot.delete_message(message.chat.id, message_id)
    else:
        bot.send_message(message.chat.id, photo_downloader(url))
        bot.delete_message(message.chat.id, message_id)


bot.infinity_polling()

file_path = './saved_videos/'
schedule.every().day.at('00:01').do(clean_old_files)
while True:
    schedule.run_pending()
