from django.db import models
# Import the reverse function
from django.urls import reverse




MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
)


# Create your models here.
class Capybara(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    personality = models.TextField(max_length=250)
    age = models.IntegerField()
    # url = models.URLField() you could also use TextField for link input 

    def __str__(self):
        return self.name 

def get_absolute_url(self):
    return reverse('detail', kwargs={'capybara_id': self.id})


# Add new Feeding model below Capymodel
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
     #add the 'choices' field options
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
      
# Create a capybara_id FK
capybara = models.ForeignKey(Capybara, on_delete=models.CASCADE)

class Meta: 
    ordering = ['-date']

def __str__(self):
    #Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
