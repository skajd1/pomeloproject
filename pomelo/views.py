from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

def Home(request):
    return render(request, 'pomelo/home.html')

def SUBMIT(request):
    url = URL.objects.create(address = request.POST["url_input"], text_data = "for test")
    return HttpResponseRedirect(reverse('pomelo:result', args = (url.id,))) 

class ResultsView(generic.DetailView):
    model = URL
    template_name = 'pomelo/result.html'
    context_object_name = 'url'
