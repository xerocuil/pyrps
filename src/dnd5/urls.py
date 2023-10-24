from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'dnd5'

urlpatterns = [
  path('', views.index, name='index'),
  # Characters
  path('characters', views.list_characters, name='list_characters'),
  path('char/add', views.add_char, name='add_char'),
  path('char/sheet/<int:charid>', views.character_sheet, name='character_sheet'),
  path('char/edit/<int:charid>', views.edit_char, name='edit_char'),
  path('avatar/edit/<int:charid>', views.edit_avatar, name='edit_avatar'),
  # Classes
  path('classes', views.list_classes, name='list_classes'),
  path('class/<int:class_id>', views.edit_class, name='edit_class'),
  # Equipment
  path('armor', views.listArmor, name='listArmor'),
  path('weapons', views.listWeapons, name='listWeapons'),
  # Reference
  path('reference', views.reference, name='reference'),
  path('reference/arcane', views.ref_arcane, name='ref_arcane'),
  path('reference/combat', views.ref_combat, name='ref_combat'),
  path('reference/equipment', views.ref_equipment, name='ref_equipment'),
  path('reference/general', views.ref_general, name='ref_general'),
]