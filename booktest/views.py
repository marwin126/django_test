from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo,HeroInfo
# Create your views here.
def index(request):
    #return HttpResponse("index")
    return render(request,'booktest/index.html',)
def books(request):
    books=BookInfo.objects.all()
    return render(request,'booktest/books.html',{'books':books})

def detail(request,bid):
    # 根据图书编号对应图书
    book=BookInfo.objects.get(id=int(bid))
    # 查找book图书中的所有英雄信息
    heros=book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})