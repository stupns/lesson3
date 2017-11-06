from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, Template
# Create your views here.


# def detail(request):
#     return HttpResponse('Well work')
"""

def detail(request):
    my_dict = {'fav_color': 'blue'}
    my_template = 'My favorite color is {{ fav_color }}'
    c = Context(my_dict)
    t = Template(my_template)
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)

"""

# def detail(request):
#     c = Context({'fav_color':'blue'})
#     t = Template('my favorite color {{ fav_color }}')
#     return  HttpResponse(t.render(c))

def detail(request):
    c = Context({'name':'Богдан'})
    t = loader.get_template('file.html')
    return HttpResponse(t.render(c))