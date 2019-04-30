#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json


def loadConf():
    with open("wechatConf.zqconfig", 'r') as wechatConf:
        settings = json.load(wechatConf)

        print(settings)
        corpid = settings['corpid']
        corpsecret = settings['corpsecret']
        return corpid, corpsecret

#
# if __name__ == '__main__':
#     test = loadConf()
#     print(test[0], test[1])
