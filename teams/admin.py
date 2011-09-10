from soccer.teams.models import Team, Stadium
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
    list_display = ("short_name", "city", "founded", "defunct")
    search_fields = ("name", "nickname", "city", )
    list_filter = ("league__confederation", "league", "defunct", )


class StadiumAdmin(admin.ModelAdmin):
    list_display = ("name", "opened", "location", "capacity")

admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium, StadiumAdmin)
