from django.db import models

class Stadium(models.Model):
    """
    Just a stadium model. 
    """
    
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # Would be nice to have a pointfield.

    opened = models.DateField(null=True)
    capacity = models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    
    
