from soccer.feeds.models import Feed

def update_feeds():
    for feed in Feed.objects.all():
        feed.fetch()


if __name__ == "__main__":
    update_feeds()
