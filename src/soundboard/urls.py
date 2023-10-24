from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'soundboard'

urlpatterns = [
  path('', views.index, name='index'),
  # Mechs
  path('b/<int:board_id>/<str:header>', views.board, name='board'),
  path('tracks/', views.list_music, name='list_music'),
  path('track/<int:music_id>', views.view_track, name='view_track'),
]