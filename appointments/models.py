from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time_slot = models.TimeField()

    class Meta:
        ordering = ['date', 'time_slot']