from django.contrib import admin

from rent.models import Car
from rent.models import CarImages

admin.site.register(Car)
admin.site.register(CarImages)