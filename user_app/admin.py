from django.contrib import admin
from .models import UserProfile, AppUser

# Register your models here.
admin.site.register([UserProfile, AppUser])