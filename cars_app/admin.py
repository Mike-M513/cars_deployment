from django.contrib import admin
from .models import Car, CarModel

# Register your models here.
admin.site.register([Car, CarModel])