from django.contrib import admin

from soccer.drafts.models import Draft, Pick

class PickAdmin(admin.ModelAdmin):
    list_display = ("number", "name", "player", "team", "draft")
    
    # Draft filter isn't working...
    #list_filter = ("draft",)


admin.site.register(Draft)
admin.site.register(Pick, PickAdmin)

