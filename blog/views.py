from django.shortcuts import render
from blog.models import MyPost
from django.template import loader, Context
from django.http import HttpResponse


# Create your views here.

def mypost(request):
    posts = MyPost.objects.all()
    t = loader.get_template('home.html')
    c = Context({'post': posts})
    return HttpResponse(t.render(c))