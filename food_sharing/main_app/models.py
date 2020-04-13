from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User 

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    exp = models.CharField("Expiry Date",max_length=10)
    count = models.CharField("How much is available", max_length=10)
    location = models.CharField("Pick-up location",max_length=100)
    contact_name = models.CharField("Contact person",max_length=100)
    tele = models.CharField("Contact number",max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('show_one', kwargs={'food_id': self.id})
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return supper().form_valid(form) 


class Comments(models.Model):
    content = models.CharField(max_length=100)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    food = models.ForeignKey(Food, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Photo for food_id: {self.food_id} @{self.url}"         