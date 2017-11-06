from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, Template
# Create your views here.

def fav(request):
    t = loader.get_template('types.html')
    rem = {}
    rem['rem'] = 'Sobaka'
    class Zoo():
        pass
    fav1 = Zoo()
    fav1.dog = 'Name dog'
    c = Context({'rem': rem,
                 'fav1': fav1})
    return HttpResponse(t.render(c))