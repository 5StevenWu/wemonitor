#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import requests
import re
from send2alimail import sendmail
import time

app = Flask(__name__)


@app.route('/')
def index():
    return 'mail110'


@app.route('/mail')
def mail():
    return '发送邮件报警'


def passimsa():
    response = requests.get('http://www.imsa.cn')
    # response = requests.get('http://cca.imsa.cn')
    pagetext = response.text
    title = '中国国际象棋协会综合服务管理平台'
    res = re.search(title, pagetext)
    if res:
        requests.get('127.0.0.1:5000',)


if __name__ == '__main__':
    # app.run(debug=True)
    while True:
        passimsa()
        time.sleep(300)
