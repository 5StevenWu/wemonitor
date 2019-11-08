#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,request

app=Flask(__name__)


@app.route('/')
def index():
    return 'mail110'

@app.route('/mail')
def mail():
    request.get
    return '发送邮件报警'


if __name__ == '__main__':
    app.run(debug=True)



