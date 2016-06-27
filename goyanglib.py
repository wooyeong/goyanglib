#!/usr/bin/env python3

import sys, locale, os
import json
import urllib.request as urlreq
from bs4 import BeautifulSoup, UnicodeDammit
from contextlib import suppress

from twx.botapi import TelegramBot, ReplyKeyboardMarkup

class TelegramBroadcaster():
    """
    Setup the bot
    """
    def __init__(self):
        self.bot = TelegramBot('<BOT_KEY>')
        self.bot.update_bot_info().wait()
        self.user_id = int(<CHANNEL_KEY>) # channel goyanglib
        print(self.bot.username)

    def send(self, message):
        result = self.bot.send_message(self.user_id, message).wait()
        print(result)

if __name__ == '__main__':
    try:
        with open('progress.json', 'r') as fp:
            memory = json.load(fp)
    except FileNotFoundError as e:
        memory = {'last': 0}
        try:
            with open('progress.json', 'w') as outfile:
                json.dump(memory, outfile)
        except FileNotFoundError as e2:
            quit()


    html = urlreq.urlopen('http://www.goyanglib.or.kr/center/comu/comuProgram.asp')
    #html = urlreq.urlopen('http://www.goyanglib.or.kr/center/comu/comuProgram.asp?cpage=2')
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.select(".line2 > table > tbody > tr")
    updated = False

    for i, elem in enumerate(lists):
        #print("%d: %s" % (i, elem))
        elem = list(elem.find_all('td'))
        #print(elem)

        num = int(elem[0].string)
        #title = elem[1].select("a")[0].string
        title = elem[1].text.strip()
        # elem[2] => progress or status
        status = elem[2].find('img')['alt']
        lib = elem[3].string
        name = elem[4].string
        date = elem[5].string

        if lib != "행신도서관":
            continue

        if memory['last'] < num:
            memory['last'] = num
            updated = True
        else:
            continue;

        print("%d: num: %d, title: %s, status: %s, lib: %s, name: %s, date: %s" % (i, num, title, status, lib, name, date))
        push_message = "새로운 민원: [%d] %s" % (num, title)
        TelegramBroadcaster().send(push_message)

    if updated:
        push_message = "보러가기: http://www.goyanglib.or.kr/center/comu/comuProgram.asp"
        TelegramBroadcaster().send(push_message)

    try:
        with open('progress.json', 'w') as outfile:
            json.dump(memory, outfile)
    except FileNotFoundError as e2:
        quit()

