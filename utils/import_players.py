
from BeautifulSoup import BeautifulSoup
import itertools
import urllib

letters = "abcdefghijklmnopqrstuvwxyz"

players_url = "http://www.mlssoccer.com/players/%s/%s"

def get_players_from_page(url):
    text = urllib.urlopen(url).read()
    soup = BeautifulSoup(text)
    tds = soup.findAll("td", {"class": "mpl-player active"})
    anchors = []
    for td in tds:
        anchors.extend(td.findAll("a"))
    d = dict([(e.contents[0], e['href']) for e in anchors])
    return d

def get_players():
    urls = {}
    for letter in letters:
        for n in itertools.count(1):
            url = players_url % (letter, n)
            d = get_players_from_page(url)
            urls.update(d)
            print d.keys()
            if d == {}:
                break
    return urls
            


    
