from django.db import models

# Create your models here.
class Appointment(models.Model):
    time=models.DateTimeField()
    description=models.CharField(max_length=640)
