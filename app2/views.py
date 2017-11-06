from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseServerError
from app2.models import Reliz
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from django.template import Context,Template,loader
from django.template import RequestContext

# Create your views here.
'''
# def detail(request):
#     return HttpResponse('nice work')

#
# def detail(request):
#     return HttpResponseNotFound('не існує')

# def detail(request, app2id):
#     return HttpResponseServerError('failed server')

# def detail(request, app2id):
#     try:
#         p = Reliz.objects.get(id=app2id)
#         return HttpResponse(p.title)
#     except Reliz.DoesNotExist:
#         return HttpResponseNotFound('page not found')

# def detail(request, app2id):
#     p = get_object_or_404(Reliz, id = app2id)
#     return HttpResponse(p.title)
'''

# def detail(request, app2id):
#     p = get_object_or_404(Reliz, id=1)
#     t = loader.get_template('detali.html')
#     c = Context({'lol': p})
#     return HttpResponse(t.render(c))

def reliz_list(request):
    pl = get_list_or_404(Reliz)
    t = loader.get_template('list.html')
    c = Context({'list': pl})
    return HttpResponse(t.render(c))

'''
def latest(request):
    p = Reliz.objects.latest()
    t = loader.get_template('latest.html')
    c = Context({
        'title':p.title,
        'avtor':p.avtor,
        'date':p.pub_date,
        'link':p.get_absolute_url(),
    })
    return HttpResponse(t.render(c))
'''

# def latest(request):
#     p = Reliz.objects.latest()
#     t = loader.get_template('latest.html')
#     title = p.title
#     date = p.pub_date
#     avtor = p.avtor
#     link = p.get_absolute_url()
#     c = Context(locals())
#     c['mu'] = 'cow'
#     c['ky'] = 'coza'
#     return HttpResponse(t.render(c))

def latest1(request):
    p = Reliz.objects.latest()
    return render_to_response('latest.html', {'press': p},context_instance=RequestContext(request))

def detail(request, app2id):
    p = get_object_or_404(Reliz, id=1)
    t = loader.get_template('detali.html')
    c = RequestContext(request,{'lol': p})
    return HttpResponse(t.render(c))