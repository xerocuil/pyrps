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
  # Cclass
  path('classes', views.listClasses, name='listClasses'),
  path('class/<int:class_id>', views.viewClass, name='viewClass'),
  # Equipment
  path('armor', views.listArmor, name='listArmor'),
  path('weapons', views.listWeapons, name='listWeapons'),
]