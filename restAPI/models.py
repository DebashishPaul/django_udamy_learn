from django.db import models

# Create your models here.

class MovieData(models.Model):

    def __str__(self):
        return self.name
    
    #id auto generate
    name = models.CharField(max_length=200, null=False)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=100, default = 'actions')