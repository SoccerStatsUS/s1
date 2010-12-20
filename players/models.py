from django.db import models

from soccer.places.models import Country
from soccer.players.aliases import mapping
from soccer.utils.bios import load_bios
from soccer.utils.scrapers import soccernet, nbcsports


class PersonManager(models.Manager):
    def get_person(self, name):
        if name in mapping:
            name = mapping[name]
        return Person.objects.get(name=name)

    def fix_birthdates(self):
        no_birthdates = Person.objects.filter(birthdate=None)
        bios = load_bios()
        l = [p.get_birthdate(bios) for p in no_birthdates]
        print len([e for e in l if e])

    def fix_birthplaces(self):
        no_birthplaces = Person.objects.filter(birthplace='')
        bios = load_bios()
        l = [p.get_birthplace(bios) for p in no_birthplaces]
        print len([e for e in l if e])


class Person(models.Model):

    # Identity
    name = models.CharField(max_length=500)
    full_name = models.CharField(max_length=500)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    nickname = models.CharField(max_length=100, blank=True)

    # Stats
    height = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=250, null=True, blank=True)
    nationality = models.ForeignKey(Country)

    # Cruft
    mls_slug = models.CharField(max_length=250, blank=True)

    objects = PersonManager()

    class Meta:
        ordering = ('last_name',)

    @property
    def get_name(self):
        if self.nickname:
            return self.nickname
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return self.name

    def get_reverses(self):
        """All aliases for a given person."""
        return [self.name] + [k for (k,v) in mapping.items() if v==self.name]


    def get_birthdate(self, bios):
        for name in self.get_reverses():
            if name in bios:
                bio = bios[name]
                self.birthdate = bio['birthdate']
                print self.name, self.birthdate
                self.save()
                return True

    def get_birthplace(self, bios):
        for name in self.get_reverses():
            if name in bios:
                bio = bios[name]
                self.birthplace = bio['birthplace']
                print self.name, self.birthplace
                self.save()
                return True


    def __unicode__(self):
        return self.name

class SoccernetBioManager(models.Manager):

    def unloaded_players(self):
        loaded_ids = set([e.soccernet_id for e in SoccernetBio.objects.all()])
        bios = soccernet.load_profiles()
        for k in bios.keys():
            if k in loaded_ids:
                bios.pop(k)

        return bios

    def load_players(self):
        for k, v in self.unloaded_players().items():
            v['soccernet_id'] = k
            sb = SoccernetBio(**v)
            sb.save()
        self.set_nationalities()

    def no_countries(self):
        return SoccernetBio.objects.filter(nationality=None)

    def set_nationalities(self):
        nc = self.no_countries()

        d = {}
        for e in Country.objects.all():
            d[e.name] = e

        if nc.count():
            for e in nc:
                bp = e.birthplace
                if "," in bp:
                    country = bp.split(",")[-1].strip()
                else:
                    country = bp.strip()

                if country in d:
                    e.nationality = d[country]
                    e.save()


                
class SoccernetBio(models.Model):

    name = models.CharField(max_length=500)
    height = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=250, null=True, blank=True)
    nationality = models.ForeignKey(Country, null=True)

    soccernet_id = models.IntegerField(null=True, blank=True)

    objects = SoccernetBioManager()

    class Meta:
        ordering = ('-birthdate',)

    def __unicode__(self):
        return self.name



class GenericBioManager(models.Manager):

    def unloaded_players(self, source):
        loaded_ids = set([e.source_id for e in GenericBio.objects.filter(source=source)])
        if source == 'soccernet':
            bios = soccernet.load_profiles()
        elif source == 'nbcsports':
            bios = nbcsports.load_profiles()
        else:
            bios = {}

        for k in bios.keys():
            if k in loaded_ids:
                bios.pop(k)

        return bios

    def load_players(self, source):
        for k, v in self.unloaded_players(source).items():
            v['source_id'] = k
            v['source'] = source
            sb = GenericBio(**v)
            sb.save()
        self.set_nationalities()

    def no_countries(self):
        return GenericBio.objects.filter(nationality=None)

    def set_nationalities(self):
        nc = self.no_countries()

        d = {}
        for e in Country.objects.all():
            d[e.name] = e

        if nc.count():
            for e in nc:
                bp = e.birthplace
                if "," in bp:
                    country = bp.split(",")[-1].strip()
                else:
                    country = bp.strip()

                if country in d:
                    e.nationality = d[country]
                    e.save()

class GenericBio(models.Model):
    
    name = models.CharField(max_length=500)
    height = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=250, null=True, blank=True)
    nationality = models.ForeignKey(Country, null=True)

    source_id = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=500)

    objects = GenericBioManager()
        
    class Meta:
        ordering = ('-birthdate',)
        
    def __unicode__(self):
        return self.name

        
        

