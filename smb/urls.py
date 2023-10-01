from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'smb'

urlpatterns = [
  path('', views.index, name='index'),
  # Mechs
  path('mech/dossier/<int:mech_id>', views.dossier, name='dossier'),
  path('matches', views.list_matches, name='list_matches'),
  path('arena/<int:match_id>', views.arena, name='arena'),
  path('melee_attack/<int:attacker>', views.melee_attack, name='melee_attack'),
  path('melee_attack_result/<int:attacker>/<int:defender>', views.melee_attack_result, name='melee_attack_result'),

]