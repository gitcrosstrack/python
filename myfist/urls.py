"""myfist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/page/2003/
    path('page/2003/', views.page_2003_view),
    #http://127.0.0.1:8000/
    path('',views.index_view),
    #http://127.0.0.1:8000/page/1
    path('page/1',views.page1_view),
    #http://127.0.0.1:8000/page/2
    path('page/2',views.page2_view),
    #http://127.0.0.1:8000/page/d%
    path('page/<int:page>',views.page_an),
    #http://127.0.0.1:8000/d1/op/z1 re_path model
    re_path(r'^(?P<d1>\d{1,2})/(?P<op>\w+)/(?P<z1>\d{1,2})$',views.jsq1_view),
    #http://127.0.0.1:8000/page/d/op/z
    path("page/<int:d>/<str:op>/<int:z>",views.jsq_view),
    # 输入网址: http://127.0.0.1:8000/birthday/2/28/2008
    # 显示为:生日为:2008年2月28日
    # 输入网址: http://127.0.0.1:8000/birthday/2015/12/11
    # 显示为:生日为:2015年12月11日
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',views.bd_view),
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$',views.bd_view),


    
]
