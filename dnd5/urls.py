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
  path('characters', views.listCharacters, name='listCharacters'),
  path('csheet/<int:charid>', views.csheet, name='csheet'),
  path('edit/char/<int:charid>', views.editChar, name='editChar'),
  path('edit/avatar/<int:charid>', views.editAvatar, name='editAvatar'),
  # Classes
  path('classes', views.listClasses, name='listClasses'),
  path('class/<int:class_id>', views.viewClass, name='viewClass'),
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