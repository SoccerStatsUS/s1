from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Alias(models.Model):
    """
    Map from, e.g. 
      FC Dallas to <Team: FC Dallas>
    or
      Kamini Hillto <Player: Kamani Hill>
    """
    # probably a good idea to require a model be passed in.
    # Not sure how to use generic foreign keys.

    name = models.CharField(max_length=255)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    aliased_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.name


    
