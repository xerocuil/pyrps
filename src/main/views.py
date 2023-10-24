from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
  apps = []
  if 'soundboard' in settings.INSTALLED_APPS:
    apps.append('soundboard')
    from soundboard.models import Music, Soundboard, Sfx
    boards = Soundboard.objects.all()
    boards_count = Soundboard.objects.all().count
    music = Music.objects.order_by('-date_added')[:5]
    music_count = Music.objects.all().count
    sfx = Sfx.objects.order_by('-date_added')[:5]
    sfx_count = Sfx.objects.all().count

  '''DND5'''
  if 'dnd5' in settings.INSTALLED_APPS:
    apps.append('dnd5')
    from dnd5.models import Character
    dnd5_chars = Character.objects.order_by('-date_added')[:5]
    dnd5_chars_count =  Character.objects.all().count

  '''SMB '''
  if 'smb' in settings.INSTALLED_APPS:
    apps.append('smb')
    from smb.models import Match, Mech
    smb_matches = Match.objects.order_by('-date_added')[:5]
    smb_mechs = Mech.objects.order_by('-date_added')[:5]
    smb_mechs_count = Mech.objects.all().count

  return render(request, 'main/index.html', {
    'apps': apps,
    'boards': boards,
    'music': music,
    'music_count': music_count,
    'sfx': sfx,
    'sfx_count': sfx_count,
    'dnd5_chars': dnd5_chars,
    'dnd5_chars_count': dnd5_chars_count,
    'smb_matches': smb_matches,
    'smb_mechs': smb_mechs
  })
