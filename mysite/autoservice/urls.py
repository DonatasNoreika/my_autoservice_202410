from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("", views.index, name="index"),
    path("cars/", views.cars, name="cars"),
    path("cars/<int:car_id>", views.car, name="car"),
    path("search/", views.search, name="search"),
    path("orders/", views.OrderListView.as_view(), name="orders"),
    path("orders/<int:pk>", views.OrderDetailView.as_view(), name="order"),
    path("userorders/", views.UserOrderListView.as_view(), name="userorders"),
    path("order/new", views.OrderCreateView.as_view(), name="order_new"),
    path("orders/<int:pk>/update", views.OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete", views.OrderDeleteView.as_view(), name="order_delete"),
    path("orders/<int:order_id>/newline", views.OrderLineCreateView.as_view(), name="orderline_new"),
]
