from django.contrib import admin

from soccer.players.models import Person, SoccernetBio, GenericBio

class PersonAdmin(admin.ModelAdmin):
    list_display = ("get_name", "nationality", "birthdate", "birthplace")
    list_filter = ("nationality", )
    search_fields = ('full_name', 'nickname')


class SoccernetBioAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "birthplace")

class GenericBioAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "birthplace")
    list_filter = ('source',)


admin.site.register(Person, PersonAdmin)
admin.site.register(SoccernetBio, SoccernetBioAdmin)
admin.site.register(GenericBio, GenericBioAdmin)


