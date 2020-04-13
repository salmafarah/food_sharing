from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Food, Comments, Photo
from .forms import CommentsForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'sharewfriends'


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
    comment_form = CommentsForm()
    return render(request,'show_one.html',{'food':food, 'comment_form': comment_form})


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

def add_comment(request,food_id):
    form = CommentsForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.food_id = food_id
        new_comment.save()
    return redirect('show_one', food_id=food_id)

def add_photo(request, food_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file: 
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + "/" + photo_file.name
        try: 
            s3.upload_fileobj(photo_file,BUCKET,key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url,food_id=food_id)
            photo.save()
        except: 
            print('An error ocurred uploding an image')
    return redirect ('show_one', food_id=food_id)

def signup(request):
    error_message = ''
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request,user)
            return redirect('index')
        else: 
            error_message = 'Invalid sign up - try again SiS'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def myshares(request):
    foods = Food.objects.all()
    return render(request, 'myshares.html', {'foods': foods})

