from django.contrib import admin
# import your models here
from .models import Capybara, Feeding 

# Register your models here

admin.site.register(Capybara)
# register the new Feeding Model
admin.site.register(Feeding)
