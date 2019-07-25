from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from sendwechat.send2wechat import send_msg
from rest_framework.views import APIView
from rest_framework.response import Response

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


class sendWechat(APIView):

    def get(self, request):
        # title = request.GET.get('title')
        # content = request.GET.get('content')
        # if title:
        #     print(title, content)
        #     ret = send_msg(title, content)
        #     return HttpResponse(str(ret))
        # return HttpResponse('OK')

        return render(request,'wechat.html')

    def post(self,request,*args,**kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title:
            print(title, content)
            res = send_msg(title, content)
            print(type(res))
            return Response(res)
        return HttpResponse('测试失败')


# http://127.0.0.1:8000/sendwechat/?title='报警标题'&content='报警内容'
