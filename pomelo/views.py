from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

def Home(request):
    return render(request, 'pomelo/home.html', {})


def result(request):
    return HttpResponse("This is result")



# class HomeView(generic.DetailView): 
#     template_name = 'home.html'
#     def get_queryset(self):
#         return 
    

