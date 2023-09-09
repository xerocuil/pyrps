from django.contrib import admin

from .models import Armor, Cclass, Character, Weapon

admin.site.register(Armor)
admin.site.register(Cclass)
admin.site.register(Character)
admin.site.register(Weapon)