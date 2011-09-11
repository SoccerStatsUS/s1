from soccer.teams.models import Team, Stadium
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
    list_display = ("short_name", "city", "founded", "defunct", "real")
    search_fields = ("name", "city", )
    list_filter = ("defunct", "real", "league__confederation", "league")

    #prepopulated_fields = {"slug": ("name",)}



class StadiumAdmin(admin.ModelAdmin):
    list_display = ("name", "opened", "location", "capacity")

admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium, StadiumAdmin)
