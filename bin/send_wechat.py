#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Version20190324
# Author:xp
# blog_url:http://blog.csdn.net/wuxingpu5/
"""pip3 install urllib"""
import sys
import urllib
import urllib.request
import json
from libs.read_config import loadConf

try:
    title = sys.argv[2]
    content = sys.argv[3]
except IndexError as e:
    title = 'without_title'
    content = 'without_content'


class Token(object):
    def __init__(self, corpid, corpsecret):
        self.baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'.format(corpid,
                                                                                                       corpsecret)

    def get_token(self):
        token_file = urllib.request.urlopen(self.baseurl)
        token_data = token_file.read().decode('utf-8')
        token_json = json.loads(token_data)
        # print(token_json)
        token = token_json['access_token']
        return token


''' 企业微信的总id 微信报警应用的Secret'''
# corpid = '企业id号'
# corpsecret = '密钥'
corpid = loadConf()[0]
corpsecret = loadConf()[1]


# print(corpid,corpsecret)

def send_msg(title, conntent):
    s_token = Token(corpid=corpid, corpsecret=corpsecret).get_token()
    # print('token创建')
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(s_token)
    # toparty:部门ID   agentid:小程序应用id
    send_value = {
        "toparty": "12",
        "msgtype": "text",
        "agentid": "1000002",
        "text": {
            "content": str(title + ' // ' + conntent),
        },
        "safe": 0
    }
    send_data = json.dumps(send_value).encode('UTF-8')
    send_request = urllib.request.Request(send_url, send_data)
    reponse = urllib.request.urlopen(send_request)
    msg = reponse.read()
    print(msg.decode('utf8'))


if __name__ == '__main__':
    # pass
    # send_msg(title, content)
    send_msg('110report测试', '报警sendSMS2--TEST--from--wechat')
