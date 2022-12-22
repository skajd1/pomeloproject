from django.urls import path

from . import views

app_name = 'pomelo'

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home'),
    path('result/', views.result, name = 'result')
]