from django.db import models
from django.urls import reverse 

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    exp = models.CharField("Expiry Date",max_length=10)
    count = models.CharField("How much is available", max_length=10)
    image = models.ImageField 
    location = models.CharField("Pick-up location",max_length=100)
    contact_name = models.CharField("Contact person",max_length=100)
    tele = models.CharField("Contact number",max_length=100)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('show_one', kwargs={'food_id': self.id})


class Comments(models.Model):
    content = models.CharField(max_length=100)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.id}"


