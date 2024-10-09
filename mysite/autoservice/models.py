from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(verbose_name="Paslauga", max_length=50)
    price = models.FloatField(verbose_name="Kaina")

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.CharField(verbose_name="Gamintojas", max_length=50)
    model = models.CharField(verbose_name="Modelis", max_length=100)

    def __str__(self):
        return f"{self.make} {self.model}"


class Car(models.Model):
    plate = models.CharField(verbose_name="Valstybinis numeris", max_length=10)
    vin_code = models.CharField(verbose_name="VIN kodas", max_length=20)
    client_name = models.CharField(verbose_name="Klientas", max_length=50)
    car_model = models.ForeignKey(to="CarModel", verbose_name="Modelis", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.plate} ({self.car_model})"


class Order(models.Model):
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    car = models.ForeignKey(to="Car", verbose_name="Automobilis", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.car}"


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", verbose_name="Užsakymas", on_delete=models.CASCADE)
    service = models.ForeignKey(to="Service", verbose_name="Paslauga", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Kiekis")

    def __str__(self):
        return f"{self.service} - {self.quantity} ({self.order})"