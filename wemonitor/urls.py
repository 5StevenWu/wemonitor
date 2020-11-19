"""wemonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sendwechat import views

# from sendmail import views
# from sendsms import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.sendWechat.as_view()),
    # url(r'^sendall/', views.sendWechat.as_view()),
    url(r'^sendwechat/', views.sendWechat.as_view()),
    url(r'^api/v3/wxmonitor/', views.wxmonitor.as_view()),
    url(r'^api/v3/voiceover/', views.voiceover.as_view()),
    # url(r'^sendmail/', views.sendWechat.as_view()),
    # url(r'^sendsms/', views.sendWechat.as_view()),
]
