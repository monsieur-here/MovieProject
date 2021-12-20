from django.db import models
from django.db.models import Count


# Create your models here.
class userLogin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=500)

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=400)
    description=models.TextField()
    genres=models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True,blank=True)
    uuid=models.UUIDField()



    

