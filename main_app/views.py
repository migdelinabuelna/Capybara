



##VIEW FUNCTIONS
# #this is the equivalent of mongoose controller functions

from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Define the following import
from .models import Capybara

#Define the home view
def home(request):
    return render(request, 'home.html')
#this is just returning a string. We need to work on a database

def about(request):
    return render(request, 'about.html') #rendering to file inside templates

def capybaras_index(request):
    capybaras = Capybara.objects.all()
    return render(request, 'capybaras/index.html', { 'capybaras': capybaras })


def capybaras_detail(request, capybara_id):
    capybara = Capybara.objects.get(id=capybara_id)
    return render(request, 'capybaras/detail.html', { 'capybara': capybara })

class CapybaraCreate(CreateView):
    model = Capybara
    fields = '__all__' #this could also have been written as fields = ['name', 'location', 'personality', 'age']
    success_url = '/capybaras/'

class CapybaraUpdate(UpdateView):
    model = Capybara
    fields = ['location', 'personality', 'age']
    success_url = '/capybaras/'

class CapybaraDelete(DeleteView):
    model = Capybara
    success_url = '/capybaras/'








# Add the Cat class & list and view function below the imports
# class Capybara:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, location, personality, age, url):
#     self.name = name
#     self.location = location
#     self.personality = personality
#     self.age = age
#     self.url = url


# capybaras = [
#   Capybara('Jim', 'Colombia', 'friends with crocodiles', 9, "https://youtube.com/embed/FB9xm3ALTCQ?feature=share"),
#   Capybara('Farhana', 'Brazil', 'Chill Kappy', 2, "https://youtube.com/embed/s_VUjFDtahg?feature=share"),
#   Capybara('Shay', 'Peru', 'Coconut Doggy', 8, "https://youtube.com/embed/cqS0d_Utoqk?feature=share"),
# ]

