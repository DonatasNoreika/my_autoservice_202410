from django.contrib import admin
from .models import (Car,
                     CarModel,
                     Service,
                     Order,
                     OrderLine)

class CarAdmin(admin.ModelAdmin):
    list_display = ['plate', 'vin_code', 'client_name', 'car_model']

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'car']
    inlines = [OrderLineInLine]

# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(CarModel)
admin.site.register(Service)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
