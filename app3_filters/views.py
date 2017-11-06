
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseServerError
from app2.models import Reliz
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from django.template import Context,Template,loader
from django.template import RequestContext


'''
def filt(request):
    f = 'filter upper'
    d = 4
    t = loader.get_template('filt.html')
    c = Context({'f':f,
                 'z':d})
    return HttpResponse(t.render(c))'''

def filt(request):
    sl = 'робить слеш"'
    t = loader.get_template('filt.html')
    c = Context({'sl': sl})
    return HttpResponse(t.render(c))