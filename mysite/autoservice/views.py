from django.shortcuts import render
from django.views.generic import ListView

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


def cars(request):
    return render(request, template_name="cars.html", context={"cars": Car.objects.all()})

def car(request, car_id):
    return render(request, template_name="car.html", context={"car": Car.objects.get(pk=car_id)})

class OrderListView(ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = "orders"

