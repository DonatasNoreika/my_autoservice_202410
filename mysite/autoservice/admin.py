from django.contrib import admin
from .models import (Car,
                     CarModel,
                     Service,
                     Order,
                     OrderLine)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class CarAdmin(admin.ModelAdmin):
    list_display = ['plate', 'vin_code', 'client_name', 'car_model']
    list_filter = ['client_name', 'car_model']
    search_fields = ['plate', 'vin_code']


class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0
    fields = ['service', 'quantity', 'line_sum']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'car']
    inlines = [OrderLineInLine]


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['service', 'quantity', 'line_sum']


# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(CarModel)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
