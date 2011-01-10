#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import datetime
from decimal import Decimal
import re
import sys

from abstract import AbstractPlayerScraper

GAME_URL = "http://sports.sportsillustrated.cnn.com/mls/boxscore.asp?gamecode=2010082103&show=pstats&ref="


class CNNSIPlayerScraper(AbstractPlayerScraper):
    FILE_PREFIX = 'cnnsi'
    PLAYER_URL = 'http://sports.sportsillustrated.cnn.com/mls/players.asp?player=%s'

    def scrape_player(self, soup):
        bio_masts = soup.findAll("table", {"class": 'shsSportMastHead'})
        if bio_masts:
            bio_mast = bio_masts[0]
        else:
            return {}

        tds = bio_mast.findAll("td", text=True)

        clean_cell = lambda t: unicode(t.replace("&nbsp;", '').replace(":", '').strip())
        cleaned_tds = [clean_cell(e) for e in tds]
        d = dict(zip(cleaned_tds[:-1], cleaned_tds[1:]))

    
        name = unicode(bio_mast.findAll("strong", {"class": 'shsPlayerName'})[0].contents[0])
        if name.endswith("-"):
            name = name[:-1]
            name = clean_cell(name)

        bio = {'name': name}

        if d['Birthdate']:
            bd = d['Birthdate']
            birthdate = datetime.datetime.strptime(bd, '%d/%m/%Y')
            bio['birthdate'] = birthdate

        if d['Birthplace']:
            bio['birthplace'] = d['Birthplace']

        if d['Height']:
            h = d['Height']
            if h.endswith("."): h = h[:-1]
            if h.endswith("m"): h = h[:-1]
            bio['height'] = int(100 * Decimal(h))

        return bio

    def scrape_stats(self, id):
        # Not running for the time being.
        return
        # Getting too many stats - also the other thing...
        soup = self.open_bio(id)

        tr = soup.findAll("tr", {"class": "shsTableTtlRow"})
        import pdb; pdb.set_trace()
        if not tr:
            return


        stats = []

        header = self.clean_list(tr[0].findAll("td", text=True))
        tr_parent = tr[0].parent

        for tr_class in ['shsRow0Row', 'shsRow1Row']:
            trs = soup.findAll("tr", {"class": tr_class})
            for tr in trs:
                numbers = filter_empty(tr.findAll("td", text=True))
                stat = zip(header, numbers)
                stats.append(stat)

        import pdb; pdb.set_trace()
        return stats
                
            

                                  
        
        


            
if __name__ == "__main__":
    s = CNNSIPlayerScraper()
    if len(sys.argv) > 1:
        s.search_profiles(int(sys.argv[1]))
    else:
        s.search_profiles()
        
                             
        
    

    


