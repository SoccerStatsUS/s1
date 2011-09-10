from soccer.leagues.models import League
from django.contrib import admin

class LeagueAdmin(admin.ModelAdmin):    
    list_display = ("name", "confederation")
    list_filter = ("confederation",)


admin.site.register(League, LeagueAdmin)

