#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version20190324
import win32gui, os, time,sys
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
# base_dir = os.path.dirname(os.path.dirname(__file__))


# print(base_dir)

def demo_top_windows():
    secLine = 90  # 文件句柄警戒值
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)#获取所有文件句柄
    print(hWndList)
    print('total window num: ', len(hWndList))
    totalwind = len(hWndList)
    if totalwind > secLine:
        from bin.send2wechat import send_msg
        send_msg('民生银行机器提示:', '文件句柄数大于' + str(secLine) + ',请确认--From电信通')
        print('句柄过多')


def portNum():
    # 端口数警戒值
    portLine = int(20)
    comandRes = os.popen('netstat -ano | findstr 8080 | find /v /c ""')
    # print(comandRes)
    portNumSum = int(comandRes.read())
    if portNumSum > portLine:
        from bin.send2wechat import send_msg
        send_msg('当前8080端口总计:' + str(portNumSum) + '个,', '请确认--From电信通', )
    print('当前8080端口总计:', portNumSum, '个')


while True:
    demo_top_windows()
    portNum()
    time.sleep(1800)
