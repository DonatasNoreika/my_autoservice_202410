from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path("", views.index, name="index"),
    path("cars/", views.cars, name="cars"),
    path("cars/<int:car_id>", views.car, name="car"),
    path("search/", views.search, name="search"),
    path("orders/", views.OrderListView.as_view(), name="orders"),
    path("orders/<int:pk>", views.OrderDetailView.as_view(), name="order"),
    path("userorders/", views.UserOrderListView.as_view(), name="userorders"),
]
