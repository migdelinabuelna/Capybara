



##VIEW FUNCTIONS
# #this is the equivalent of mongoose controller functions

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Define the following import
from .models import Capybara
#Import the FeedingForm 
from .forms import FeedingForm



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
    #instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'capybaras/detail.html', { 
        #include the capybara and feeding_form in the context 
        'capybara': capybara, 'feeding_form': feeding_form
    })

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

def add_feeding(request, capybara_id):
 # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the capybara_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.capybara_id = capybara_id
    new_feeding.save()
  return redirect('detail', capybara_id=capybara_id)

