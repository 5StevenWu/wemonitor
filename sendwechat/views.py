from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from sendwechat.send2wechat import send_msg


# Create your views here.


class sendWechat(View):

    def get(self, request):
        title = request.GET.get('title')
        content = request.GET.get('content')
        if title:
            print(title, content)
            ret = send_msg(title, content)
            return HttpResponse(str(ret))
        return HttpResponse('OK')

# http://127.0.0.1:8000/sendwechat/?title='报警标题'&content='报警内容'
