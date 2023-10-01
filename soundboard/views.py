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

  music = [{'index': 1, 'obj': board.music1}, {'index': 2, 'obj': board.music2}, {'index': 3, 'obj': board.music3}, {'index': 4, 'obj': board.music4}, {'index': 5, 'obj': board.music5}, {'index': 6, 'obj': board.music6}, {'index': 7, 'obj': board.music7}, {'index': 8, 'obj': board.music8}]

  sfx = [{'index': 1, 'obj': board.sfx1}, {'index': 2, 'obj': board.sfx2}, {'index': 3, 'obj': board.sfx3}, {'index': 4, 'obj': board.sfx4}, {'index': 5, 'obj': board.sfx5}, {'index': 6, 'obj': board.sfx6}, {'index': 7, 'obj': board.sfx7}, {'index': 8, 'obj': board.sfx8}, {'index': 9, 'obj': board.sfx9}, {'index': 10, 'obj': board.sfx10}, {'index': 11, 'obj': board.sfx11}, {'index': 12, 'obj': board.sfx12}, {'index': 13, 'obj': board.sfx13}, {'index': 14, 'obj': board.sfx14}, {'index': 15, 'obj': board.sfx15}, {'index': 16, 'obj': board.sfx16}]

  return render(request, 'soundboard/board.html', {
    'board': board,
    'music': music,
    'sfx': sfx
  })
