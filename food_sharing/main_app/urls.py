from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('shares/', views.shares, name='shares'), 
    path('shares/<int:food_id>/', views.show_one, name='show_one'),
    path('shares/create/', views.FoodCreate.as_view(), name='create_food')

]