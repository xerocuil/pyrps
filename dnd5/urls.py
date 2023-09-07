from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'dnd5'

urlpatterns = [
  path('', views.index, name='index'),
  path('edit/char/<int:char_id>', views.editChar, name='editChar'),
  path('edit/avatar/<int:char_id>', views.editAvatar, name='editAvatar'),
]