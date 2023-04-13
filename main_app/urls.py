#this is the quivalent of routers folder in mongoose


from django.urls import path 
from . import views 

#path function that will be used to define each route

urlpatterns = [
    path('', views.home, name='home'), #root path to views
    path('about/', views.about, name='about'),
    #route for capybaras index
    path('capybaras/', views.capybaras_index, name='index'),
    path('capybaras/<int:capybara_id>/', views.capybaras_detail, name='detail'),
    path('capybaras/create', views.CapybaraCreate.as_view(), name='capybaras_create'),
    path('capybaras/<int:pk>/update/', views.CapybaraUpdate.as_view(), name='capybaras_update'),
    path('capybaras/<int:pk>/delete/', views.CapybaraDelete.as_view(), name='capybaras_delete'),
    path('capybaras/<int:capybara_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('capybaras/<int:capybara_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]

#<int:capybara_id>reffers to the id of the papybara we are working with