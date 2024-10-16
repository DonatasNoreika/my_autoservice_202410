from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Service, Order, Car
from django.db.models import Q

# Create your views here.

def index(request):
    num_services = Service.objects.count()
    num_orders = Order.objects.filter(status="i").count()
    num_cars = Car.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        "num_services": num_services,
        "num_orders": num_orders,
        "num_cars": num_cars,
        "num_visits": num_visits,
    }
    return render(request, template_name="index.html", context=context)


def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, per_page=6)
    page_number = request.GET.get("page")
    paged_cars = paginator.get_page(page_number)
    return render(request, template_name="cars.html", context={"cars": paged_cars})

def car(request, car_id):
    return render(request, template_name="car.html", context={"car": Car.objects.get(pk=car_id)})

class OrderListView(ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = "orders"
    paginate_by = 4

class OrderDetailView(DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = "order"

def search(request):
    query = request.GET.get("query")
    cars_search_results = Car.objects.filter(Q(client_name__icontains=query) | Q(car_model__make__icontains=query) | Q(car_model__model__icontains=query) | Q(plate__icontains=query) | Q(vin_code__icontains=query))
    context = {
        "query": query,
        "cars": cars_search_results,
    }
    return render(request, template_name="search.html", context=context)