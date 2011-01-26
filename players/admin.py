from django.contrib import admin

from soccer.players.models import Person, GenericBio

class PersonAdmin(admin.ModelAdmin):
    # Nationality is breaking this.
    list_display = ("id", "get_name", "birthdate", "birthplace")
    list_filter = ("nationality", )
    search_fields = ('full_name', 'name', 'nickname')


class GenericBioAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "birthplace")
    list_filter = ('source',)


admin.site.register(Person, PersonAdmin)
admin.site.register(GenericBio, GenericBioAdmin)


