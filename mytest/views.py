from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseServerError
from app2.models import Reliz
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template import Context,Template,loader
# Create your views here.


def my_test_func(request):
    return HttpResponse('good luck')