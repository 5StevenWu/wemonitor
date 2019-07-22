#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def loadConf():
    with open(os.path.join(BASE_DIR, 'sendwechat/wechatConf.zqconfig'), 'r') as wechatConf:
        settings = json.load(wechatConf)
        corpid = settings['corpid']
        corpsecret = settings['corpsecret']
        return corpid, corpsecret


if __name__ == '__main__':
    test = loadConf()
    print(test[0], test[1])
