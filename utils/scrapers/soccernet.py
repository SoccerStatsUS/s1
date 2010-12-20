#!/usr/bin/env python

import datetime
from decimal import Decimal
import re

from abstract import AbstractPlayerScraper

class SoccernetPlayerScraper(AbstractPlayerScraper):
    DATA_FOLDER = 'soccernet'
    PLAYER_URL = 'http://soccernet.espn.go.com/player/_/id/%s'

    def scrape_player(self, id):
        soup = self.open_page(id)
    
        bio_div = soup.findAll("div", {"class": "profile"})[0]
        bio_li = bio_div.findAll("li")

        d = {}

        d['name'] = unicode(bio_div.findAll("h1")[0].contents[0])

        for li in bio_li:
            text = li.contents[0]
        
            try:
                text.startswith("")
            except TypeError:
                continue

            if hasattr(text, 'startswith'):
                if text.startswith("Birth Place"):
                    birthplace = text.replace("Birth Place:", '').strip()
                    if len(birthplace) == 1:
                        home_country = birthplace
                    elif len(birthplace) == 2:
                        home_country = birthplace.split(',')[1]
                    else:
                        home_country = None

                    d['birthplace'] = unicode(birthplace)
        
                if text.startswith("Birth Date"):
                    text = text.replace("Birth Date:", '').strip()
                    birthdate = datetime.datetime.strptime(text, '%b %d, %Y')
                    d['birthdate'] = birthdate
            
                if text.startswith('Height'):
                    text = text.replace("Height:", '').strip()
                    r1 = re.compile("(?P<meters>\d\.\d+)m")
                    r2 = re.compile('.*?\((?P<meters>\d\.\d+)m\)')
                    for regex in (r1, r2):
                        if regex.search(text):
                            meters_s = regex.search(text).groups()[0]
                            meters = Decimal(meters_s)
                            cm = int(100 * meters)
                            d['height'] = cm


        return d
