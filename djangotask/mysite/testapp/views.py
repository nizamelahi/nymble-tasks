from django.shortcuts import render,get_object_or_404
from .models import list
from django.http import HttpResponse, Http404,  HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.contrib import messages
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'testapp/index.html'
    context_object_name = 'lists'

    def get_queryset(self):
        """return list"""
        return list.objects.order_by('id')

def submit(request):
    list_text=request.POST['text']
    if list_text :
        list.objects.create(list_text=request.POST['text'])
        messages.success(request, 'text added')
    else :
        messages.error(request, 'unable to add')
        
    return HttpResponseRedirect(reverse('testapp:index'))

def remv(request,lpk):
    lisob=list.objects.get(pk=lpk)
    context_object_name = 'lisob'
    lisob.delete()
    messages.success(request, 'text deleted')
    return HttpResponseRedirect(reverse('testapp:index'))

def editpage(request,lpk):
    lisob=list.objects.get(pk=lpk)
    return render(request, 'testapp/editpage.html', {'obj': lisob})

def edit(request,lpk):
    lisob=list.objects.get(pk=lpk)
    lisob.list_text=request.POST['text']
    lisob.save()
    messages.success(request, 'text edited')
    return HttpResponseRedirect(reverse('testapp:index'))
