from django.contrib import admin
from .models import (Car,
                     CarModel,
                     Service,
                     Order,
                     OrderLine,
                     OrderComment,
                     Profile)

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
    readonly_fields = ['line_sum']

class OrderCommentInLine(admin.TabularInline):
    model = OrderComment
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'client', 'deadline', 'car', 'status', 'total', 'is_overdue']
    inlines = [OrderLineInLine, OrderCommentInLine]

    fieldsets = [
        ["General", {"fields": ['date', 'deadline', 'client', 'car', 'status', 'total']}]
    ]
    readonly_fields = ['date', 'total']


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['service', 'quantity', 'line_sum']


# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(CarModel)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Profile)
