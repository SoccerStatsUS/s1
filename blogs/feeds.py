from django.contrib.syndication.feeds import Feed

from soccer.blogs.models import Entry

class BlogFeed(Feed):
    num_items = 20
    feed_title = "Soccer News"
    feed_link = "/news/"
    feed_description = "News from the best soccer news sites"
    short_title = "news"

    def obj_title(self, obj):
        return obj.name

    def items(self):
        return Entry.objects.all()[self.num_items]
