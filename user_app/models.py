from django.db import models
from django.core import validators

# Create your models here.

class AppUser(models.Model):
    account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, unique=True, max_length=255)
    password = models.CharField(blank=False, validators=[validators.MinLengthValidator(8)], max_length=255)

    def __str__(self):
        return f"ID {self.account_id} - {self.first_name} {self.last_name}"
    
    def update_email(self, new_email):
        self.email = new_email
        self.save()
    
    def update_password(self, new_password):
        self.password = new_password
        self.save()

class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    account_id = models.OneToOneField(AppUser, on_delete=models.CASCADE, blank=False)
    street_name = models.CharField(blank=False, max_length=255)
    street_number = models.CharField(blank=False, max_length=255)
    zip_code = models.CharField(blank=False, max_length=255)
    city = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return f"ID {self.profile_id}"
    
    def update_address(self, new_street_name, new_street_number, new_zip_code, new_city):
        self.street_name = new_street_name
        self.street_number = new_street_number
        self.zip_code = new_zip_code
        self.city = new_city
        self.save()