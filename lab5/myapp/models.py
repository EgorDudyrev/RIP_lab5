from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)


class  Hotel(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    description = models.CharField(max_length=255,null=True)
    adress = models.CharField(max_length=30)


class Booking(models.Model):
    user = models.ForeignKey(User)
    hotel = models.ForeignKey(Hotel)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
