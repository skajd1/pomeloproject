from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .validator import is_url_valid
from .get_html_text import get_html_text
from .get_html_text_v2  import get_html_text_v2
from .extract_summary import summary



def Home(request):
    return render(request, 'pomelo/home.html')

def SUBMIT(request):
    r_address = '_'
    if request.POST.get('select', 'text_selected') == 'text_selected' :
        text = request.POST.get('user_input')
    else :
        r_address = request.POST.get('user_input', False)    
        if not r_address or not is_url_valid(r_address) :
            return render(request, 'pomelo/home.html', {'error' : "올바른 주소 형식을 입력하세요."})
        text = get_html_text_v2(r_address)
        return render(request, 'pomelo/text.html', {'text' : text} )
        
    url = URL.objects.create(address = r_address, text_data = summary(text))
    #return HttpResponseRedirect(reverse('pomelo:result', args = (url.id,))) 
    return render(request, 'pomelo/result.html', {'text' : summary(text)} )

class ResultsView(generic.DetailView):
    model = URL
    template_name = 'pomelo/result.html'
    context_object_name = 'url'

class TextView(generic.DetailView):
    model = URL
    template_name = 'pomleo/text.html'
    context_object_name = 'url'