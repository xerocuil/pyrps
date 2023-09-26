import os

from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Armor, Character, Cclass, Weapon
from .forms import AvatarForm, CclassForm, CharacterForm

from .rules import Arcane, Combat, Equipment, General

from PIL import Image


# D&D5 Main
def index(request):
  latest_characters = Character.objects.order_by('-date_modified')[:5]
  latest_classes = Cclass.objects.order_by('-date_added')[:5]
  latest_weapons = Weapon.objects.order_by('-date_added')[:5]
  return render(request, 'dnd5/index.html', {
    'latest_characters': latest_characters,
    'latest_classes': latest_classes,
    'latest_weapons': latest_weapons
  })


# Characters
def character_sheet(request, charid):
  character = get_object_or_404(Character, charid=charid)
  ability_modifiers = General.AbilityModifier.LIST
  return render(
    request=request,
    template_name="dnd5/character/sheet.html",
    context = {
      'character': character,
      'ability_modifiers': ability_modifiers,
    })

def add_char(request):
  if request.method == "POST":
    try:
      char_form = CharacterForm(request.POST, request.FILES)
      if char_form.is_valid():
        char_form.save()
        messages.success(request, 'Character was successfully added!', extra_tags='safe')
    except (IntegrityError, DatabaseError) as err:
      messages.error(request, err)
    return redirect("dnd5:list_characters")
  else:
    char_form = CharacterForm()

  return render(
    request=request,
    template_name="dnd5/character/add.html",
    context={
      'char_form': char_form
    }
  )

def edit_char(request, charid):
  character = get_object_or_404(Character, charid=charid)

  if request.method == 'POST':
    char_form = CharacterForm(request.POST, request.FILES, instance=character)
    if char_form.is_valid():
      char_form.save()
      messages.success(request, character.name + ' was successfully edited.')
      print(character)
    else:
      messages.error(request, char_form.errors)
    return redirect("dnd5:list_characters")
  else:
    char_form = CharacterForm(instance=character)

  return render(
    request=request,
    template_name="dnd5/character/edit_char.html",
    context = {
      'character': character,
      'char_form': char_form
    }
  )

def edit_avatar(request, charid):
  character = get_object_or_404(Character, charid=charid)

  ## Avatar form
  if request.method == 'POST':
    avatar_form = AvatarForm(request.POST, request.FILES, instance=character)
    if avatar_form.is_valid():
      avatar_form.save()
      messages.success(request, 'Sucessfully changed avatar for ' + character.name)

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
        
        size = (128, 128)

        ## Save thumbnail and remove original
        with Image.open(image_file) as im:
          im.thumbnail(size)
          im.save(newfile, 'PNG')
          os.remove(image_file)
          character.avatar = newentry
          character.save()
    else:
      messages.error(request, avatar_form.errors)
    return redirect("dnd5:edit_char", character.charid)
  else:
    avatar_form = AvatarForm(instance=character)

  return render(
    request=request,
    template_name="dnd5/character/edit_avatar.html",
    context = {
      'character': character,
      'avatar_form': avatar_form
    }
  )

def list_characters(request):
  page_title = "Characters"
  characters = Character.objects.order_by('-date_modified')
  return render(request, 'dnd5/character/list.html', {
    'page_title': page_title,
    'characters': characters
  })


# Classes
def list_classes(request):
  classes = Cclass.objects.all()
  return render(request, 'dnd5/class/list.html', {
    'classes': classes
    })

def edit_class(request, class_id):
  cclass = get_object_or_404(Cclass, pk=class_id)
  if request.method == 'POST':
    class_form = CclassForm(request.POST, request.FILES, instance=cclass)
    if class_form.is_valid():
      class_form.save()
      messages.success(request, cclass.name + ' was successfully edited.')
      print(cclass)
    else:
      messages.error(request, class_form.errors)
    return redirect("dnd5:list_classes")
  else:
    class_form = CclassForm(instance=cclass)

  return render(request, 'dnd5/class/edit.html', {
    'cclass': cclass,
    'class_form': class_form
    })


# Equipment
def listArmor(request):
  armor = Armor.objects.all()
  return render(request, 'dnd5/armor.html', {
    'armor': armor
    })

def listWeapons(request):
  weapons = Weapon.objects.all()
  return render(request, 'dnd5/weapons.html', {
    'weapons': weapons
    })


# Reference
def reference(request):
  page_title = "Reference"
  return render(request, 'dnd5/reference/index.html', {
    'page_title': page_title})

def ref_arcane(request):
  page_title = "Arcane"
  arcane_schools = Arcane.School.LIST
  area_of_effect = Arcane.AreaOfEffect.LIST
  spell_components = Arcane.Component.LIST
  return render(request, 'dnd5/reference/arcane.html', {
    'page_title': page_title,
    'arcane_schools': arcane_schools,
    'area_of_effect': area_of_effect,
    'spell_components': spell_components
  })

def ref_combat(request):
  page_title = "Combat"
  challenge_ratings = Combat.ChallengeRating.LIST
  conditions = Combat.Condition.LIST
  damage_types = Combat.DamageType.LIST
  monster_types = Combat.MonsterType.LIST
  return render(request, 'dnd5/reference/combat.html', {
    'page_title': page_title,
    'challenge_ratings': challenge_ratings,
    'conditions': conditions,
    'damage_types': damage_types,
    'monster_types': monster_types
  })

def ref_equipment(request):
  page_title = "Equipment"
  equipment_categories = Equipment.Category.LIST
  armor_properties = Equipment.ArmorProperty.LIST
  weapon_properties = Equipment.WeaponProperty.LIST
  return render(request, 'dnd5/reference/equipment.html', {
    'page_title': page_title,
    'equipment_categories': equipment_categories,
    'armor_properties': armor_properties,
    'weapon_properties': weapon_properties
  })

def ref_general(request):
  page_title = "General"
  abilities = General.Ability.LIST
  ability_modifiers = General.AbilityModifier.LIST
  character_advancement = General.CharacterAdvancement.LIST
  return render(request, 'dnd5/reference/general.html', {
    'page_title': page_title,
    'abilities': abilities,
    'ability_modifiers': ability_modifiers,
    'character_advancement': character_advancement
  })