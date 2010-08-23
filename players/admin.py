from django.contrib import admin

from soccer.players.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "nationality", "birthdate")
    list_filter = ("nationality", )

admin.site.register(Person, PersonAdmin)


