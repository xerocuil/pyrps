import os

from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Character, Cclass
from .forms import AvatarForm, CharacterForm

from PIL import Image

def index(request):
  recently_added = Character.objects.order_by('date_added')
  # Character.getStrMod
  # Character.getDexMod
  return render(request, 'dnd5/index.html', {
    'recently_added': recently_added
  })

def editChar(request, char_id):
  character = get_object_or_404(Character, pk=char_id)

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

## Edit Avatar
def editAvatar(request, char_id):
  character = get_object_or_404(Character, pk=char_id)

  ## Avatar form
  if request.method == 'POST':
    avatar_form = AvatarForm(request.POST, request.FILES, instance=character)
    if avatar_form.is_valid():
      avatar_form.save()
      messages.success(request, character.name + ' was successfully edited.')

      ### Avatar file settings
      # appdir = str(settings.BASE_DIR)
      # avatarurl = 'dnd5/avatars'
      # mediadir = os.path.join(appdir, 'media')
      # avatardir = os.path.join(mediadir, avatarurl)
      # image_file = os.path.join(appdir + character.avatar.url)
      # filename, ext = os.path.splitext(image_file)
      # newfilename = str(character.char_id) + '.png'
      # newfile = os.path.join(avatardir, newfilename)
      # newentry = avatarurl + '/' + newfilename
      
      # size = (256, 256)

      ### Save thumbnail and remove original
      # with Image.open(image_file) as im:
        # im.thumbnail(size)
        # im.save(newfile, 'PNG')
        # os.remove(image_file)
        # character.avatar = newentry
        # character.save()

          
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

