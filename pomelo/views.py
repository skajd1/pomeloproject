from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .validator import is_url_valid






def Home(request):
    return render(request, 'pomelo/home.html')

def SUBMIT(request):
    r_address = request.POST["url_input"]

    if not r_address or not is_url_valid(r_address) :
        return render(request, 'pomelo/home.html', {'error' : "올바른 주소 형식을 입력하세요."})
    url = URL.objects.create(address = r_address, text_data = "for test")


    return HttpResponseRedirect(reverse('pomelo:result', args = (url.id,))) 

class ResultsView(generic.DetailView):
    model = URL
    template_name = 'pomelo/result.html'
    context_object_name = 'url'
