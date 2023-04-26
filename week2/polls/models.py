from django.db import models

# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text='Enter the exact time!')

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.TimeField(help_text="enter the exact time")
    comments = models.CharField(max_length=500)