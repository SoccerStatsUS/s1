#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import datetime
from decimal import Decimal
import re
import sys
import urllib2

from abstract import AbstractPlayerScraper

GAME_URL = "http://sports.sportsillustrated.cnn.com/mls/boxscore.asp?gamecode=2010082103&show=pstats&ref="


import datetime
# All we want to do is get the score of a game.
class CNNSIScoreboardScraper(object):

    COMPETITION_URLS = {
        "Major League Soccer": "http://sports.sportsillustrated.cnn.com/mls/scoreboard_daily.asp",
        "Bundesliga": "http://sports.sportsillustrated.cnn.com/bund/scoreboard_daily.asp",
        }

    TEST_DATE = datetime.date(2011,8,27)

    def __init__(self):
        pass

    def format_date(self, date):
        return date.strftime("%Y%m%d")

    def get_date_page(self, date, competition):
        url = "%s?gameday=%s" % (self.COMPETITION_URLS[competition], self.format_date(date))
        html = urllib2.urlopen(url).read()
        return BeautifulSoup(html)


    def process_date(self, date, competition):
        soup = self.get_date_page(date, competition)
        matches = [e.parent for e in soup.findAll("tr", "shsMatchDayRow")]
        results = []
        for match in matches:
            # Need to handle bad dates anyway...
            if date < datetime.date.today():
                try:
                    scores = match.find("td", "shsTotD shsSBScoreTD").contents[0]
                except:
                    import pdb; pdb.set_trace()
                home_score, away_score = [int(e) for e in scores.strip().split("-")]
                home = match.find("td", "shsNamD shsHomeTeam").find("a").contents[0]
                away = match.find("td", "shsNumD shsAwayTeam").find("a").contents[0]
                d = {
                    "home": home,
                    "away": away,
                    "home_score": home_score,
                    "away_score": away_score,
                    "date": date,
                    }
                results.append(d)

        return results


    def main(self):
        self.process_date(self.TEST_DATE)
        

    
def create_games(date, competition, create=True):
    from soccer.lineups.models import Game, Team
    css = CNNSIScoreboardScraper()
    results = css.process_date(date, competition)
    for result in results:

        try:
            home_team = Team.objects.get_team(result['home'])
        except:
            import pdb; pdb.set_trace()
            print result['home']

        try:
            away_team = Team.objects.get_team(result['away'])
        except:
            import pdb; pdb.set_trace()
            print result['away']

        if create:
            Game.objects.create(
                date=date,
                home_team=home_team,
                away_team=away_team,
                home_score=result['home_score'],
                away_score=result['away_score'],
                )


def create_span(start, end, competition, create=True):
    while start < end:
        create_games(start, competition, create)
        start += datetime.timedelta(days=1)


def do_year(year, competition):
    start = datetime.date(year, 1, 1)
    end = datetime.date(year + 1, 1, 1)
    create_span(start, end, competition)
        

    



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
        
                             
        
    

    


