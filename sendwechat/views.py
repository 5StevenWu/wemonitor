from django.shortcuts import render, HttpResponse, redirect
from django.views import View


# Create your views here.


class sendWechat(View):
    def get(self,request):
        # pass

        return HttpResponse('OK')
