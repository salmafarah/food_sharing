from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('shares/', views.shares, name='shares'), 
    path('shares/myshares/', views.myshares, name='myshares'),
    path('shares/<int:food_id>/', views.show_one, name='show_one'),
    path('shares/create/', views.FoodCreate.as_view(), name='create_food'), 
    path('shares/<int:pk>/update/', views.FoodUpdate.as_view(),name='update_food'), 
    path('shares/<int:pk>/delete/', views.FoodDelete.as_view(), name='delete_food'),
    path('shares/<int:food_id>/add_comment/', views.add_comment, name='add_comment'),
    path('shares/<int:food_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup')
    
]