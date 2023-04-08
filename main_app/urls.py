#this is the quivalent of routers folder in mongoose


from django.urls import path 
from . import views 

#path function that will be used to define each route

urlpatterns = [
    path('', views.home, name='home'), #root path to views
    path('about/', views.about, name='about'),
    #route for capybaras index
    path('capybaras/', views.capybaras_index, name='index'),
]

