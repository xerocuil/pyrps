import os
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, render, redirect
from PIL import Image

from .models import Match, Mech, MechClass
# from .forms import MechForm, MechClassForm

# SMB Main
def index(request):
  latest_mechs = Mech.objects.order_by('name')[:5]
  return render(request, 'smb/index.html', {
    'latest_mechs': latest_mechs
  })

# Mech
def dossier(request, mech_id):
  mech = get_object_or_404(Mech, mech_id=mech_id)
  return render(request, 'smb/mech/dossier.html', {
    'mech': mech
  })

# Match
def list_matches(request):
  matches = Match.objects.all()
  return render(request, 'smb/match/list.html', {
    'matches': matches
  })

def arena(request, match_id):
  match = get_object_or_404(Match, pk=match_id)
  return render(request, 'smb/match/arena.html', {
    'match': match
  })

def melee_attack(request, attacker):
  attacker = get_object_or_404(Mech, mech_id=attacker)
  mechs = Mech.objects.exclude(mech_id=attacker.mech_id)
  return render(request, 'smb/match/select.html',{
    'attacker': attacker,
    'mechs': mechs
    })

def melee_attack_result(request, attacker, defender):
  attacker = get_object_or_404(Mech, mech_id=attacker)
  defender = get_object_or_404(Mech, mech_id=defender)
  dmg = 1
  defender.shields = defender.shields - dmg
  print(defender.shields)
  defender.save()
  return render(request, 'smb/match/result.html',{
    'attacker': attacker,
    'defender': defender,
    })
# def melee_attack(self, attacker, defender):
#   dmg = attacker.strength
#   defender.hull_points = defender.hull_points - dmg
#   print(defender.hull_points)