from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Traveler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Hotel(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    description = models.CharField(max_length=255,null=True)

class Booking(models.Model):
    user = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


@admin.register(Traveler)
class TravelerAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

