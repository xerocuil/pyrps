from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'smb'

urlpatterns = [
  path('', views.index, name='index'),
  # Mechs
  path('mech/dossier/<int:mech_id>', views.dossier, name='dossier'),

]