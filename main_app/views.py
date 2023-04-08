



##VIEW FUNCTIONS
# #this is the equivalent of mongoose controller functions

from django.shortcuts import render

#Add the following import
from django.http import HttpResponse

#Define the following import
from django.http import HttpResponse

#Define the home view
def home(request):
    return render(request, 'home.html')
#this is just returning a string. We need to work on a database

def about(request):
    return render(request, 'about.html') #rendering to file inside templates

def capybaras_index(request):
    return render(request, 'capybaras/index.html', { 'capybaras': capybaras })

# Add the Cat class & list and view function below the imports
class Capybara:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, location, personality, age):
    self.name = name
    self.location = location
    self.personality = personality
    self.age = age

capybaras = [
  Capybara('Jim', 'Colombia', 'friends with crocodiles', 9),
  Capybara('Farhana', 'Brazil', 'Chill Capybara', 2),
  Capybara('Shay', 'Peru', 'Shy Capybara', 8)
]
