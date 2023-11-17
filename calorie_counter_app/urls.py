
from django.urls import path
from . import views
urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('add/', views.add_food, name='add_food'),
    path('delete/', views.delete_food, name='delete_food'),
]
