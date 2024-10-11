from django.shortcuts import render
from .models import Service, Order, Car

# Create your views here.

def index(request):
    num_services = Service.objects.count()
    num_orders = Order.objects.filter(status="i").count()
    num_cars = Car.objects.count()
    context = {
        "num_services": num_services,
        "num_orders": num_orders,
        "num_cars": num_cars,
    }
    return render(request, template_name="index.html", context=context)