from lib2to3.fixes.fix_input import context

from django.shortcuts import render , get_object_or_404
from django.template.context_processors import request

from .models import News, Category


# Create your views here.






def news_list(request):
    news_list = News.objects.all()
    context = {
        "news_list":news_list

    }



    return render(request,'news/news_list.html', context)


def news_detail(request):
    news = get_object_or_404(News, id=id, status=News.status.Published)
    context = {
        "news": news
    }

    return render(request, 'news/news_detail.html', context)




def homePageViews(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        "news":news,
        "categories":categories
    }

    return render(request, 'news/home.html',context)


def contactPageWiev(request):
    context = {

    }
    return render(request, 'news/contact.html', context)