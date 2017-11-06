from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, Template

# Create your views here.
def myfunc(request):
    t = loader.get_template('home.html')
    c = Context({'name':'serhii'})
    return HttpResponse(t.render(c))