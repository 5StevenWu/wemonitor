#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version20190324
import win32gui, os, time


def demo_top_windows():
    secLine = 90  # 文件句柄警戒值
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    print(hWndList)
    print('total window num: ', len(hWndList))
    totalwind = len(hWndList)
    if totalwind > secLine:
        from bin.send_wechat import send_msg
        send_msg('民生银行机器提示:', '文件句柄数大于' + str(secLine) + ',请确认--From电信通')
        print('句柄过多')


def portNum():
    # 端口数警戒值
    portLine = int(20)
    comandRes = os.popen('netstat -ano | findstr 8080 | find /v /c ""')
    # print(comandRes)
    portNumSum = int(comandRes.read())
    if portNumSum > portLine:
        from bin.send_wechat import send_msg
        send_msg('当前8080端口总计:' + str(portNumSum) + '个,', '无', )
    print('当前8080端口总计:', portNumSum, '个')


while True:
    if __name__ == '__main__':
        demo_top_windows()
        portNum()
    time.sleep(180)
