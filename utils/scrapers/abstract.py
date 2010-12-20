#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup, HTMLParseError
import cPickle
import datetime
from decimal import Decimal
import logging
import os
import re
import sys
import time
import urllib2

LOG_DIR = "/home/chris/www/soccer/logs"
LOG_FORMAT = "%(asctime)s\t%(process)d\t%(levelname)s\t%(filename)s\t%(message)s"

logger = logging.getLogger('scraper')
logger.setLevel(logging.DEBUG)

to_file = logging.FileHandler(
    os.path.join(LOG_DIR, 'scraper'))
to_file.setFormatter(logging.Formatter(LOG_FORMAT))

logger.addHandler(to_file)


class AbstractPlayerScraper(object):
    DATA_DIR = '/home/chris/www/soccer/data'
    DATA_FOLDER = None
    PLAYER_URL = None

    def __init__(self):
        pass

    @property
    def profiles_path(self):
        return os.path.join(self.DATA_DIR, self.DATA_FOLDER, 'profiles')

    @property
    def max_path(self):
        return os.path.join(self.DATA_DIR, self.DATA_FOLDER, 'max')

    @property
    def lock_path(self):
        return os.path.join(self.DATA_DIR, self.DATA_FOLDER, 'lock')

    def is_locked(self):
        return os.path.exists(self.lock_path)

    def create_lock(self):
        f = open(self.lock_path, 'w')
        f.close()

    def unlock(self):
        os.remove(self.lock_path)


    def get_max(self):
        return int(open(self.max_path).read())

    def set_max(self, num):
        f  = open(self.max_path, 'w')
        f.write(str(num))
        f.close()

    def load_profiles(self):
        if os.path.isfile(self.profiles_path):
            f = open(self.profiles_path)
            d = cPickle.load(f)
            f.close()
            return d
        else:
            return {}

    def save_profiles(self, d):
        d1 = self.load_profiles()
        f = open(self.profiles_path, 'w')
        d1.update(d)
        cPickle.dump(d1, f)
        f.close()
    
    def search_profiles(self, count=1000):
        if self.is_locked():
            return

        self.create_lock()
        d = self.load_profiles()
        
        start = self.get_max()
        end = start + count
        
        i = 0
        print "processing from %s to %s" % (start, end)
        for num in range(start, end):
            i += 1
            time.sleep(1.5)
            try:
                scraped = self.scrape_player(num)
                if 'birthdate' in scraped:
                    if 'birthplace' in scraped:
                        d[num] = scraped
            except HTMLParseError:
                print "Couldn't parse %s" % num
                logger.debug("Couldn't parse %s" % num)
            except urllib2.HTTPError:
                print "Received HTTP Error for %s" % num
                logger.error("Received HTTP Error for %s" % num)
                self.unlock()
                return

            if i % 25 == 0:
                print "Downloading %s" % (start + i)
                self.set_max(end)
                self.save_profiles(d)

        self.set_max(end)
        self.save_profiles(d)
        self.unlock()
        return d

    def scrape_player(self, id):
        return NotImplementedError

    def open_page(self, id):
        url = self.PLAYER_URL % id
        html = urllib2.urlopen(url).read()
        return BeautifulSoup(html)    

