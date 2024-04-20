from django.db import models
from cars_app.models import Car
from user_app.models import AppUser

# Create your models here.
class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    advertisement_date = models.DateField(blank=False)
    seller_account_id = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=False)
    car_id = models.OneToOneField(Car, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"ID {self.advertisement_id} - {self.advertisement_date}"
    
    def ChangeDate(self, new_date):
        self.advertisement_date= new_date
        self.save()
        