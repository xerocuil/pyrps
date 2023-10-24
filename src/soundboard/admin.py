from django.contrib import admin

from .models import Music, Sfx, Soundboard, Tag

admin.site.register(Music)
admin.site.register(Sfx)
admin.site.register(Soundboard)
admin.site.register(Tag)
