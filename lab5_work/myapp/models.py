from django.db import models
from django.contrib.auth.models import AbstractBaseUser as BUser

# Create your models here.
class User(BUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)#, unique=True)
    email = models.EmailField(default='def@rip.ru')
    phone = models.CharField(max_length=11,default='0')

    def get_full_name(self):
        return "{} {}".format(self.last_name, self.first_name)
    def get_short_name(self):
        return self.first_name

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email','last_name','first_name']

class Hotel(BUser):
    name = models.CharField(max_length=30)#, unique=True)
    email = models.EmailField(default='def@rip.ru')
    adress = models.CharField(max_length=30)
    description = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=11,default='0')

    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name

    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email','adress']

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
