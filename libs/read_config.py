#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json

homedir = os.path.dirname(os.path.dirname(__file__))  # D:\code\zenthought\wemonitor  #此种写法可以在任意非当前路径调用
conf_file = 'conf/wechatConf.zqconfig'
realdir = os.path.join(homedir, conf_file)  # D:/code/zenthought/wemonitor\conf/wechatConf.zqconfig
print(realdir)


def loadConf():
    with open(realdir, 'rU') as wechatConf:
        settings = json.load(wechatConf)
        corpid = settings['corpid']
        corpsecret = settings['corpsecret']
        return corpid, corpsecret


if __name__ == '__main__':
    test = loadConf()
    print(test[0], test[1])
