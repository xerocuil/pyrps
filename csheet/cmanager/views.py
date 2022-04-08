from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from .models import Mech, MechClass, Page, Player

def home(request):
	return render(request, 'cmanager/home.html', {
		'home': page
	})

def page(request, slug):
	page = get_object_or_404(Page, slug=slug)
	return render(request, 'cmanager/page.html', {
		'page': page
	})

def player_detail(request, id):
	player = get_object_or_404(Player, pk=id)
	return render(request, 'cmanager/player_detail.html', {
			'player': player
		})

def players(request):
	players = Player.objects.order_by('name')
	return render(request, 'cmanager/players.html', {
			'players': players
		})

def mech_classes(request):
	mech_classes = MechClass.objects.order_by('name')
	return render(request, 'cmanager/classes.html', {
			'mech_classes': mech_classes
		})

def mech_detail(request, id):
	mech = get_object_or_404(Mech, pk=id)
	return render(request, 'cmanager/mech_detail.html', {
			'mech': mech
		})

def mechs(request):
	mechs = Mech.objects.order_by('name')
	return render(request, 'cmanager/mechs.html', {
			'mechs': mechs
		})