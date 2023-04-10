from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Capybara(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    personality = models.TextField(max_length=250)
    age = models.IntegerField()
    # url = models.URLField()

    def __str__(self):
        return self.name 

def get_absolute_url(self):
    return reverse('detail', kwargs={'capybara_id': self.id})