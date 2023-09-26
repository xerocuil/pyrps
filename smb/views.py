import os
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, render, redirect
from PIL import Image

from .models import Mech, MechClass
# from .models import Armor, Character, Cclass, Weapon
# from .forms import AvatarForm, CclassForm, CharacterForm

# SMB Main
def index(request):
  latest_mechs = Mech.objects.order_by('name')[:5]
  return render(request, 'smb/index.html', {
    'latest_mechs': latest_mechs,
  })

# Characters
def dossier(request, mech_id):
  mech = get_object_or_404(Mech, mech_id=mech_id)
  # ability_modifiers = General.AbilityModifier.LIST
  return render(
    request=request,
    template_name="smb/mech/dossier.html",
    context = {
      'mech': mech,
    })