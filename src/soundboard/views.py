import os
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, render, redirect
from PIL import Image

from .models import Music, Sfx, Soundboard, Tag

def index(request):
  boards = Soundboard.objects.order_by('-date_added')
  music = Music.objects.order_by('-date_added')[:5]
  sfx = Sfx.objects.order_by('-date_added')[:5]
  return render(request, 'soundboard/index.html', {
    'boards': boards,
    'music': music,
    'sfx': sfx
  })


# Boards

''' View '''
def board(request, board_id, header):
  page_header = header
  board = get_object_or_404(Soundboard, pk=board_id)
  return render(request, 'soundboard/board/view.html', {
    'board': board,
    'page_header': page_header
  })


# Music

''' List '''
def list_music(request):
  music = Music.objects.all()
  tags = Tag.objects.all()
  return render(request, 'soundboard/music/list.html', {
    'music': music,
    'tags': tags
  })

''' View '''
def view_track(request, music_id):
  music = get_object_or_404(Music, pk=music_id)
  return render(request, 'soundboard/music/view.html', {
    'music': music
  })