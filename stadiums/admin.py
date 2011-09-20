from soccer.stadiums.models import Stadium
from django.contrib import admin

class StadiumAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name", "location")


admin.site.register(Stadium, StadiumAdmin)
