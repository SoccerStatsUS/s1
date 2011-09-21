from soccer.video.models import Video
from django.contrib import admin

class VideoAdmin(admin.ModelAdmin):
    list_display = ("url", "name")
    search_fields = ("url", "name", "description")


admin.site.register(Video, VideoAdmin)
