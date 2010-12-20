import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://www.soccerbase.com/results3.sd?gameid=618301"

def fix_bad_script_tags(text):
    """Soccerbase has some badly formatted script tags.  Fix them."""
    return text.replace("scri'+'pt", "script")
        

def scrape_page(url):
    html = urllib2.urlopen(url).read()
    html = fix_bad_script_tags(html)
    soup = BeautifulSoup(html)
    return soup
    

