#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def loadConf():
    with open('wechatConf.zqconfig', 'r') as wechatConf:
        settings = json.load(wechatConf)
        # corpid = settings['corpid']
        # corpsecret = settings['corpsecret']
        passwd=settings["passwd"]
        return passwd


if __name__ == '__main__':
    test = loadConf()
    print(test)
