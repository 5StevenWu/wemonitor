from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from sendwechat.send2wechat import send_msg
from rest_framework.views import APIView
from rest_framework.response import Response
from dwebsocket.decorators import accept_websocket,require_websocket
import time,json

# Create your views here.

class sendWechat(APIView):

    def get(self, request):
        title = request.GET.get('title')
        content = request.GET.get('content')
        if title:
            print(title, content)
            ret = send_msg(title, content)
            return HttpResponse(str(ret))
        return HttpResponse('欢迎使用报警平台')


# http://127.0.0.1:8000/sendwechat/?title='报警标题'&content='报警内容'

class wxmonitor(APIView):

    def get(self, request):
        return render(request, 'wechat.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title:
            print(title, content)
            res = send_msg(title, content)
            print(type(res))
            return Response(res)
        return HttpResponse('测试失败')

class voiceover(APIView):

    def get(self, request):
        return render(request, 'voiceover.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title:
            print(title, content)
            res = send_msg(title, content)
            print(type(res))
            return Response(res)
        return HttpResponse('测试失败')




@accept_websocket
def websocket_vv(request,msg=1):
    if request.method=='GET':
        return render(request,'vvws.html')
    if request.is_websocket():
        while True:
            time.sleep(1)
            dit={
                "time":time.strftime('%Y %m %d %H%M%S', time.localtime(time.time()))
            }
            request.websocket.send(json.dumps(dit))

#from dwebsocket.decorators import accept_websocket,require_websocket

#@accept_websocket
# def test_websocket(request):
#     if request.is_websocket():
#         while 1:
#             time.sleep(1) ## 向前端发送时间
#             dit = {
#                 'time':time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
#             }
#             request.websocket.send(json.dumps(dit))
