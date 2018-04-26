from django.db import models

# Create your models here.
class Appointment(models.Model):
    time=models.DateTimeField()
    description=models.CharField(max_length=640)
    #let's make the admin kinda better to use
    def __str__(self):
        return "%s at %s"%(self.description, self.time)
