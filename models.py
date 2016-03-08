
from django.db import models


class Restaurant(models.Model):
    id_restaurant = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    open_current_day = models.CharField(max_length=10)
    is_active = models.BooleanField
    street = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    www = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    id_meal = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField
    is_vege = models.BooleanField

    def __str__(self):
        return self.name


class Ingridients(models.Model):
    id_ingridient = models.AutoField(primary_key=True)
    id_meal = models.models.ManyToManyField(IdMeal, through='Meal')
    name = models.CharField(max_length=50)
    is_active = models.BooleanField

    def __str__(self):
        return self.name


class Comments(models.Model):
    id_comment = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    spice_rate = models.DecimalField(max_digits=5, decimal_places=1)
    rank = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.name
