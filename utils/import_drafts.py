from BeautifulSoup import BeautifulSoup
import urllib2


def open_wikipedia(url):
    request = urllib2.Request(url)
    request.add_header("User-Agent", "Wikipedia Override")
    opener = urllib2.build_opener()
    return opener.open(request).read()

def process_table(table):
    ths = table.findAll("th")
    picks = []
    for th in ths:
        try:
            int(th.contents[0])
            picks.append(th)
            
