from django.urls import path

from . import views

app_name = 'pomelo'

urlpatterns = [
    #path('', views.HomeView.as_view(), name= 'home'),
    path('', views.Home, name = 'home'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'result'),
    path('submit/',views.SUBMIT, name ='submit')
]