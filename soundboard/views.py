import os
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, render, redirect
from PIL import Image

from .models import Music, Sfx, Soundboard

def index(request):
  boards = Soundboard.objects.all()
  return render(request, 'soundboard/index.html', {
    'boards': boards
  })

# Board
def board(request, board_id):
  board = get_object_or_404(Soundboard, pk=board_id)

  return render(request, 'soundboard/board.html', {
    'board': board,
  })
