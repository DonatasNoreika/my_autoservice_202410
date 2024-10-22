from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from PIL import Image

import pytz

utc = pytz.UTC


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Nuotrauka", upload_to="profile_pics", default="profile_pics/default.png")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

class Service(models.Model):
    name = models.CharField(verbose_name="Paslauga", max_length=50)
    price = models.FloatField(verbose_name="Kaina")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"


class CarModel(models.Model):
    make = models.CharField(verbose_name="Gamintojas", max_length=50)
    model = models.CharField(verbose_name="Modelis", max_length=100)

    def __str__(self):
        return f"{self.make} {self.model}"

    class Meta:
        verbose_name = "Modelis"
        verbose_name_plural = "Modeliai"


class Car(models.Model):
    plate = models.CharField(verbose_name="Valstybinis numeris", max_length=10)
    vin_code = models.CharField(verbose_name="VIN kodas", max_length=20)
    client_name = models.CharField(verbose_name="Klientas", max_length=50)
    car_model = models.ForeignKey(to="CarModel", verbose_name="Modelis", on_delete=models.SET_NULL, null=True,
                                  blank=True)
    photo = models.ImageField(verbose_name="nuotrauka", upload_to="cars", null=True, blank=True)
    description = HTMLField(verbose_name="Aprašymas", null=True, blank=True)

    def __str__(self):
        return f"{self.plate} ({self.car_model})"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"


class Order(models.Model):
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    car = models.ForeignKey(to="Car", verbose_name="Automobilis", on_delete=models.CASCADE, related_name="orders")
    CHOICES = [
        ("a", "Administruojamas"),
        ("v", "Vykdomas"),
        ("i", "Įvykdytas"),
        ("p", "Atmestas"),
    ]
    status = models.CharField(verbose_name="Būsena", max_length=1, choices=CHOICES, default="a")
    client = models.ForeignKey(to=User, verbose_name="Klientas", on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(verbose_name="Gražinimo laikas", null=True, blank=True)

    def is_overdue(self):
        return self.deadline and self.deadline.replace(tzinfo=utc) < datetime.today().replace(tzinfo=utc)

    is_overdue.short_description = 'Praleistas terminas'

    def total(self):
        total_sum = 0
        for line in self.lines.all():
            total_sum += line.line_sum()
        return total_sum

    total.short_description = 'Bendra suma'

    def __str__(self):
        return f"{self.date} - {self.car}"

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", verbose_name="Užsakymas", on_delete=models.CASCADE, related_name="lines")
    service = models.ForeignKey(to="Service", verbose_name="Paslauga", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Kiekis")

    def line_sum(self):
        return self.service.price * self.quantity

    line_sum.short_description = 'Suma'

    def __str__(self):
        return f"{self.service} - {self.quantity} ({self.order})"

    class Meta:
        verbose_name = "Eilutė"
        verbose_name_plural = "Eilutės"


class OrderComment(models.Model):
    order = models.ForeignKey(to="Order", verbose_name="Užsakymas", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(to=User, verbose_name="Komentatorius", on_delete=models.CASCADE)
    date_created = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Atsiliepimas", max_length=2000)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']
