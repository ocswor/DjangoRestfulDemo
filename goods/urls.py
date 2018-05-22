# -*- coding: utf-8 -*-
# @Time    : 18-5-22 上午9:59
# @Author  : yijialiang

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from goods import views

urlpatterns = [
    url(r'^goods/$', views.GoodsList.as_view()),
    url(r'^goods/(?P<pk>[0-9]+)/$', views.GoodsDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)