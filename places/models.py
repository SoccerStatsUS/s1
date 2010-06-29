from django.db import models

# Create your models here.


class City(models.Model):
    slug = models.CharField(max_length=50, unique=True, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, default='U.S.A.')
    location = models.PointField(null=True, blank=True)

    
