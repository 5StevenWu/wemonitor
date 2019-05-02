#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json

base_dir = os.path.dirname(os.path.dirname(__file__))
# print(base_dir)


def loadConf():
    with open("../conf/wechatConf.zqconfig", 'r') as wechatConf:
        settings = json.load(wechatConf)
        corpid = settings['corpid']
        corpsecret = settings['corpsecret']
        return corpid, corpsecret


if __name__ == '__main__':
    test = loadConf()
    print(test[0], test[1])
