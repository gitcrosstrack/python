from django.http import HttpResponse


def page_2003_view(request):

    html ="<h1>this is the first page <h1>"
    return HttpResponse(html)
def index_view(request):
    html ="<h1>这是我的首页<h1>"
    return HttpResponse(html)
def page1_view(request):
    html ="<h1>这是第一个<h1>"
    return HttpResponse(html)
def page2_view(request):
    html ="<h1>这是第2个<h1>"
    return HttpResponse(html)
def page_an(request,page):
    html ="这是第%s个网页"%(page)
    return HttpResponse(html)
def jsq_view(request,d,op,z):
    if op not in["add","su","mult"]:
        return HttpResponse("wrong")
    key=0
    if op == "add":
        key=d+z
    elif op == "su":
        key=d-z
    elif op == "mult":
        key =d*z
    return HttpResponse("结果为%s"%(key))
def jsq1_view(request,d1,op,z1):
    html="d1:%s,op:%s,z1:%s"%(d1,op,z1)
    return HttpResponse(html)
def bd_view(request,y,m,d):
    html="你的生日是%s年%s月%s日"%(y,m,d)
    return HttpResponse(html)
# def bd1_view(request,m,d,y):
#     html="你的生日是%s月%s日%s年"%(m,d,y)
#     return HttpResponse(html)