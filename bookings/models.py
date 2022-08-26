from distutils.command.upload import upload
from django.db import models
from accounts.models import Account
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    address = models.CharField(max_length=300)
    images = models.ImageField(upload_to='photos/rooms')

    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    available_time = models.TimeField()
    
    def __str__(self):
        return self.available_time.strftime('%I:%M %p')
   

class Booking(models.Model):
    name = models.CharField(max_length=120)
    booking_date = models.DateField()
    # booking_time = models.TimeField()
    # booking_date = models.DateField()
    booking_time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=True)
    booking_person = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name