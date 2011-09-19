from soccer.places.models import Country
from soccer.players.models import Person

# What the heck is the point of this stuff?

def p():
    u = Person.objects.filter(nationality=None).order_by("name")
    for e in u[:120]:
        print e.name
    print u.count()
    

def nick(name, nickname):
    p = Person.objects.get(name=name)
    p.nickname = nickname
    p.save()

def sn(name, country, nickname):
    s(name, country)
    nick(name, nickname)

def sid(name, id):
    p = Person.objects.get(name=name)
    c = Country.objects.get(id=id)
    p.nationality = c
    p.save()

def s(name, country):
    m = {
        "us": "United States",
        "tt": "Trinidad and Tobago"
        }
    if country in m:
        country = m[country]

    p = Person.objects.get(name=name)
    c = Country.objects.get(name=country)
    p.nationality = c
    p.save()

br = lambda n: s(n,'Brazil')
ar = lambda n: s(n,'Argentina')
us = lambda n: s(n,'us')
tt = lambda n: s(n,'tt')
c = lambda n: s(n, 'Canada')
uk = lambda n: s(n, "United Kingdom")
j = lambda n: s(n, "Jamaica")
sa = lambda n: s(n, "South Africa")
g = lambda n: s(n, "Ghana")
m = lambda n: s(n, "Mexico")
cr = lambda n: s(n, "Costa Rica")
es = lambda n: s(n, "El Salvador")
nz = lambda n: s(n, "New Zealand")
