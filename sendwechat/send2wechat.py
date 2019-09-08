#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Version20190324
# Author:xp
# blog_url:http://blog.csdn.net/wuxingpu5/
"""pip3 install urllib"""
import os
import sys
import urllib
import urllib.request
import json

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
from sendwechat.read_config import loadConf

try:
    # 脚本执行传入的参数  例如:来自zbx的shell脚本调用  传入第二个参数为报警标题 第三个为报警内容
    title = sys.argv[2]
    content = sys.argv[3]
except IndexError as e:
    title = 'without_title'
    content = 'without_content'


class Token(object):
    def __init__(self, corpid, corpsecret):
        '''

        :param corpid:  微信id
        :param corpsecret: 微信密码
        '''
        self.baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'.format(corpid,
                                                                                                       corpsecret)

    def get_token(self):
        '''
        请求微信api
        :return: 返回token
        '''
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
        "toparty": "16",
        "msgtype": "text",
        "agentid": "1000011",
        "text": {
            "content": str(title + ' // ' + conntent),
        },
        "safe": 0
    }
    send_data = json.dumps(send_value).encode('UTF-8')
    send_request = urllib.request.Request(send_url, send_data)
    reponse = urllib.request.urlopen(send_request)
    msg = reponse.read()
    print('发送结果',msg.decode('utf8'))
    return msg.decode('utf8')


if __name__ == '__main__':
    # pass
    # send_msg(title, content)
    send_msg('110report测试', '报警sendSMS2--TEST--from--wechat')
