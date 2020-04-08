from django.db import models
from django.urls import reverse 

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    exp = models.CharField(max_length=10)
    count = models.CharField(max_length=10)
    image = models.ImageField
    location = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    tele = models.CharField(max_length=100)


    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('show_one', kwargs={'food_id': self.id})



