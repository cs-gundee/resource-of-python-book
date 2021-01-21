from django.db import models

# Create your models here.
class Center(models.Model):
    code = models.CharField(max_length=2)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})" 

class Transport(models.Model):
    # origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Center, on_delete=models.CASCADE, related_name="origin_city")
    destination = models.ForeignKey(Center, on_delete=models.CASCADE, related_name="dest_city")
    #destination = models.CharField(max_length=64)
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.origin} -с {self.destination}"

# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell


# from transport.models import Transport
# t = Transport(origin="Ulaanbaatar", destination="Arkhangai", distance=520)
# t = Transport(origin="Улаанбаатар", destination="Архангай", distance=520)
# t.save()
# trans = Transport.objects.all()

# clear screen:
# import os
# os.system('cls||clear')

class Passenger(models.Model):
    lastname = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)    
    transports = models.ManyToManyField(Transport, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.lastname} овогтой {self.firstname}"