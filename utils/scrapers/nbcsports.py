#!/usr/bin/env python

import datetime
from decimal import Decimal
import re

from abstract import AbstractPlayerScraper


class NBCSportsPlayerScraper(AbstractPlayerScraper):
    DATA_FOLDER = 'nbcsports'
    PLAYER_URL = 'http://scores.nbcsports.msnbc.com/epl/players.asp?player=%s'

    def scrape_player(self, id):
        soup = self.open_page(id)
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


            
if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_profiles(int(sys.argv[1]))
    else:
        search_profiles()
        
                             
        
    

    

