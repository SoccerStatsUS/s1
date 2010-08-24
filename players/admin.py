from django.contrib import admin

from soccer.players.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ("get_name", "nationality", "birthdate", "birthplace")
    list_filter = ("nationality", )
    search_fields = ('full_name', 'nickname')

admin.site.register(Person, PersonAdmin)


