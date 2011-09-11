from soccer.leagues.models import League
from django.contrib import admin

class LeagueAdmin(admin.ModelAdmin):    
    list_display = ("name", "confederation", "country")
    list_filter = ("confederation", "country")


admin.site.register(League, LeagueAdmin)

