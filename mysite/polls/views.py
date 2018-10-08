 #allow to send response to the us
from django.shortcuts import get_object_or_404, render
from .models import Article
from django.http import HttpResponse


def hello(request):
    articles= Article.objects.all()
    return render(request, 'index.html',{'dec':articles})

def article_detail(request,slug):
    return HttpResponse(slug)
