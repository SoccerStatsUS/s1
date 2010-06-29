import datetime
import feedparser
import re

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

# Checks to make sure the articles pulled in are soccer-related.
SOCCER_WORDS = "soccer", "goal", "midfielder", "goalkeeper", "offside", "penalty kick"
SOCCER_RE = re.compile("|".join(SOCCER_WORDS))



def parse_date_string(s):
    s = s.split(".")[0] # cut off microseconds
    s = s.split("-")[0] # date ranges being given for some reason?
    d, t = s.split("T")
    year, month, day = [int(e) for e in d.split("-")]
    hour, minute, second = [int(e) for e in t.split("-")]
    return datetime.datetime(year, month, day, hour, minute, second)

class TaggedItem(models.Model):

    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    content_object = generic.GenericForeignKey()

    class Meta:
        ordering = ["tag"]

    def __unicode__(self):
        return self.tag



class Feed(models.Model):

    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    last_updated = models.DateTimeField()
    soccer_only = models.BooleanField(default=False)

    def fetch(self):
        feed = feedparser.parse(self.url)
        self.last_updated = datetime.datetime.now()
        self.save()
        
        for e in feed.entries:
            content = e.content[0].value
            if 
            Entry.objects.create(
                title=e.title,
                summary=e.summary, 
                source=self,
                author=e.author,
                pub_date=parse_date_string(e.published),
                url = e.link,
                )

    def __unicode__(self):
        return self.name


class Entry(models.Model):

    title = models.CharField(max_length=100)
    summary = models.TextField()
    
    source = models.ForeignKey(Feed, related_name="entries")
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    url = models.CharField(max_length=100)

    tags = generic.GenericRelation(TaggedItem)

        
    def __unicode__(self):
        return "%s - %s" % (self.source.name, self.title)
        
        
    
