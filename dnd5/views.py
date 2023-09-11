import os

from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Armor, Character, Cclass, Weapon
from .forms import AvatarForm, CharacterForm

from PIL import Image

def index(request):
  latest_characters = Character.objects.order_by('-date_added')[:5]
  latest_classes = Cclass.objects.order_by('-date_added')[:5]
  latest_weapons = Weapon.objects.order_by('-date_added')[:5]
  return render(request, 'dnd5/index.html', {
    'latest_characters': latest_characters,
    'latest_classes': latest_classes,
    'latest_weapons': latest_weapons
  })


## Characters
def csheet(request, charid):
  character = get_object_or_404(Character, pk=charid)

  return render(
    request=request,
    template_name="dnd5/csheet.html",
    context = {
      'character': character,
    })

def editChar(request, charid):
  character = get_object_or_404(Character, pk=charid)

  if request.method == 'POST':
    char_form = CharacterForm(request.POST, request.FILES, instance=character)
    if char_form.is_valid():
      char_form.save()
      messages.success(request, character.name + ' was successfully edited.')
      print(character)
    else:
      messages.error(request, char_form.errors)
    return redirect("dnd5:index")
  else:
    char_form = CharacterForm(instance=character)

  return render(
    request=request,
    template_name="dnd5/editChar.html",
    context = {
      'character': character,
      'char_form': char_form
    }
  )

def editAvatar(request, charid):
  character = get_object_or_404(Character, pk=charid)

  ## Avatar form
  if request.method == 'POST':
    avatar_form = AvatarForm(request.POST, request.FILES, instance=character)
    if avatar_form.is_valid():
      avatar_form.save()
      messages.success(request, character.name + ' was successfully edited.')

      if character.avatar:

        ## Avatar file settings
        appdir = str(settings.BASE_DIR)
        avatarurl = 'dnd5/avatars'
        mediadir = os.path.join(appdir, 'media')
        avatardir = os.path.join(mediadir, avatarurl)
        image_file = os.path.join(appdir + character.avatar.url)
        filename, ext = os.path.splitext(image_file)
        newfilename = str(character.charid) + '.png'
        newfile = os.path.join(avatardir, newfilename)
        newentry = avatarurl + '/' + newfilename
        
        size = (256, 256)

        ## Save thumbnail and remove original
        with Image.open(image_file) as im:
          im.thumbnail(size)
          im.save(newfile, 'PNG')
          os.remove(image_file)
          character.avatar = newentry
          character.save()
    else:
      messages.error(request, avatar_form.errors)
    return redirect("dnd5:editChar", character.id)
  else:
    avatar_form = AvatarForm(instance=character)

  return render(
    request=request,
    template_name="dnd5/editAvatar.html",
    context = {
      'character': character,
      'avatar_form': avatar_form
    }
  )

def listCharacters(request):
  characters = Character.objects.all()
  return render(request, 'dnd5/characters.html', {
    'characters': characters
  })


## Classes
def listClasses(request):
  classes = Cclass.objects.all()
  return render(request, 'dnd5/classes.html', {
    'classes': classes
    })

def viewClass(request, class_id):
  c = get_object_or_404(Cclass, pk=class_id)
  return render(request, 'dnd5/viewClass.html', {
    'c': c
    })


## Armor
def listArmor(request):
  armor = Armor.objects.all()
  return render(request, 'dnd5/armor.html', {
    'armor': armor
    })


## Weapons
def listWeapons(request):
  weapons = Weapon.objects.all()
  return render(request, 'dnd5/weapons.html', {
    'weapons': weapons
    })