from django.contrib import admin

from .models import Armor, Cclass, Character, Race, Weapon

admin.site.register(Armor)
admin.site.register(Cclass)
admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Weapon)