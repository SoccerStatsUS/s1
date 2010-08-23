from soccer.teams.models import Team, Stadium
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
    list_display = ("short_name",)
    list_filter = ("league", )

admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium)
