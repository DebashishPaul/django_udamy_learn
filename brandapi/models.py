from django.db import models

# Create your models here.
class BrandModel(models.Model):
    #id
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    followers = models.FloatField()
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    