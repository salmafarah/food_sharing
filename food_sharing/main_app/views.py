from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Food

# Create your views here.

# class Food: 
#     def __init__(self,name,description, exp, count, image, location, contact_name, tele):
#         self.name = name
#         self.description = description
#         self.exp = exp
#         self.count = count
#         self.image = image
#         self.location = location
#         self.contact_name = contact_name
#         self.tele = tele

# foods = [
#     Food('Canned lentil soup', 'I have 1 canned soup available', '2029/01/11', '1 can', 'https://imgur.com/CEUW2yL.jpg', 'Toronto, Ontario', 'James', '416-435-6578'),
#     Food('Ramen noddle', 'Chicken and Beef ramen noddles', '2024/12/30', '12 pak', 'https://imgur.com/ywy11IY.jpg', 'Ottawa, Ontario', 'Lul','647-982-3721' ),
#     Food('Linguine Pasta', "I can give away 2 packs of pasta", '2025/05/14','2pak', 'https://imgur.com/GbjIIa9.jpg', 'Waterloo, Ontario', 'Ayan', '647-223-5496'),
#     Food('Chips', 'Pack of chips', '2030/07/25','12 pak', 'https://imgur.com/jli7RNb.jpg','Toronto, Ontario', 'Sarah', '416-123-0976')
# ]

def home(request):
    return render(request,'home.html')

def shares(request):
    foods = Food.objects.all()
    return render(request, 'index.html', {'foods':foods})

def show_one(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request,'show_one.html',{'food':food})

class FoodCreate(CreateView):
    model = Food
    fields = '__all__'
    success_url = '/shares/<int:food_id>/'

class FoodUpdate(UpdateView): 
    model = Food 
    fields = '__all__'

class FoodDelete(DeleteView):
    model = Food 
    success_url = '/shares/'