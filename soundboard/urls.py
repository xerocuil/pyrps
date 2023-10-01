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
  path('b/<int:board_id>', views.board, name='board'),

]