from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Food: 
    def __init__(self,name,description, exp, count, image, location, contact_name, tele):
        self.name = name
        self.description = description
        self.exp = exp
        self.count = count
        self.image = image
        self.location = location
        self.contact_name = contact_name
        self.tele = tele

food = [
    Food('Canned lentil soup', 'I have 1 canned soup available', '2029/01/11', '1 can', 'https://imgur.com/CEUW2yL.jpg', 'Toronto, Ontario', 'James', '416-435-6578'),
    Food('Ramen noddle', 'Chicken and Beef ramen noddles', '2024/12/30', '12 pak', 'https://imgur.com/ywy11IY.jpg', 'Ottawa, Ontario', 'Lul','647-982-3721' ),
    Food('Linguine Pasta', "I can give away 2 packs of pasta", '2025/05/14','2pak', 'https://imgur.com/GbjIIa9.jpg', 'Waterloo, Ontario', 'Ayan', '647-223-5496'),
    Food('Chips', 'Pack of chips', '2030/07/25','12 pak', 'https://imgur.com/jli7RNb.jpg','Toronto, Ontario', 'Sarah', '416-123-0976')
]



def home(request):
    return render(request,'home.html')

def shares(request):
    return render(request, 'index.html')