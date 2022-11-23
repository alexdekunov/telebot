from telegram.ext import Updater
from settings.py import token

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater(token, use_context=True, request_kwargs=PROXY)

    mybot.start_polling()
    mybot.idle()

main()