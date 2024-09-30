from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()  # Get all cars from the database
    return render(request, 'cars/car_list.html', {'cars': cars})
