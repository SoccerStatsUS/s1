from soccer.teams.models import Team
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
    list_display = ("short_name", "city", "founded", "defunct", "real")
    search_fields = ("name", "city", )
    list_filter = ("defunct", "real", "league__confederation", "league")

admin.site.register(Team, TeamAdmin)
