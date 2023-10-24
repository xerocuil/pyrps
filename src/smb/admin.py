from django.contrib import admin

from .models import Match, Mech, MechClass

admin.site.register(Match)
admin.site.register(Mech)
admin.site.register(MechClass)
