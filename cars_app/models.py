from django.db import models

# Create your models here.
class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    make = models.CharField(blank=False, max_length=255)
    model = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return f"ID {self.car_model_id} - {self.make} {self.model}"
    
    def update_car_make(self, new_car_make):
        self.make = new_car_make
        self.save()

    def update_car_model(self, new_car_model):
        self.model = new_car_model
        self.save()

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_model_id = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    number_of_owners = models.IntegerField(blank=False)
    registration_number = models.CharField(blank=False, unique=True, max_length=255)
    manufacture_year = models.IntegerField(blank=False)
    number_of_doors = models.IntegerField(blank=False, default=5)
    mileage = models.IntegerField()

    def __str__(self):
        return f"ID {self.car_id}"
    
    def increase_number_of_owners(self, new_number_of_owners):
        self.number_of_owners = new_number_of_owners
        self.save()

    def increase_mileage(self, new_mileage):
        self.mileage = new_mileage
        self.save()