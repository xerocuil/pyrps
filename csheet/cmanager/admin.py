from django.contrib import admin

from .models import Player, Mech, MechClass, Page

admin.site.register(Player)
admin.site.register(Mech)
admin.site.register(MechClass)
admin.site.register(Page)
