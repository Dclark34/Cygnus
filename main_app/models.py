from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


#Bird Model
class Bird(models.Model):
    common_name = models.CharField(max_length=75)
    family = models.CharField(max_length=50)
    common_region = models.CharField(max_length=75)
    quantity = models.IntegerField()

    def __str__(self):
        return self.common_name
    
    def get_absolute_url(self):
        return reverse('bird-detail', kwargs={'pk':self.id})





# sighting model
class Sighting(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField('Log Date')
    notes = models.TextField(max_length= 250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birds = models.ManyToManyField(Bird, through='SightingBird')
    def __str__(self):
        return self.location #had a type error here where the str wouldnt convert the date. 
    
    def get_absolute_url(self):
        return reverse('sight-detail', kwargs={'sighting_id': self.id})




class SightingBird(models.Model):
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.bird.common_name} at {self.sighting.location}"