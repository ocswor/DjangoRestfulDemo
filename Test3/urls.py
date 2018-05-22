"""Test3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url, include
from users.views import UserViewset
from rest_framework import routers
# from goods.views import Goods
#
router = routers.DefaultRouter()

#配置goods的url
# router.register(r'goods', Goods, base_name="goods")
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'docs/', include_docs_urls(title="文档")),
    path('api/', include('goods.urls')),
    url(r'^', include(router.urls)),
]
