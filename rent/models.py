from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Car(models.Model):
    transmission_type = (
        ('A', 'Auto'),
        ('M', 'Manuel')
    )
    body_type_choices = (
        ('S', 'Sedan'),
        ('H', 'Hatchback')
    )
    fuel_type_choices = (
        ('G', 'Gasoline'),
        ('D', 'Diesel'),
        ('E', 'Electric')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    doors = models.IntegerField()
    production_year = models.DateField()
    body_type = models.CharField(max_length=10, choices=body_type_choices)
    fuel_type = models.CharField(max_length=15, choices=fuel_type_choices)
    km = models.DecimalField(max_digits=8, decimal_places=3)
    color = models.CharField(max_length=10)
    transmission = models.CharField(max_length=10, choices=transmission_type)
    plate = models.CharField(max_length=15)
    air_conditioning = models.BooleanField(default=False)
    rent_ptice = models.DecimalField(max_digits=8, decimal_places=2)
    rented_date = models.DateTimeField()
    last_rented_date = models.DateTimeField()
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.plate

def get_image_filename(instance, filename):
    id = instance.car.id
    return "carImages/%s" % (id)


class CarImages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename)

    def __str__(self):
        return self.car.plate