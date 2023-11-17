from django.shortcuts import render, redirect
from .models import FoodItem

def food_list(request):
    foods = FoodItem.objects.all()
    return render(request, 'food_list.html', {'foods' : foods})

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calorie_count = request.POST.get('calorie_count')
        return redirect('food_list')
    return render(request, 'add_food.html')

def delete_food(request, food_id):
    food = FoodItem.objects.get(pk=food_id)
    food.delete()
    return redirect('food_list')

# def total_calories(request, food_id):



# Create your views here.
# from django.http import HttpResponse
# def helloWorld(request): 
#     return HttpResponse('Hello, world!')

