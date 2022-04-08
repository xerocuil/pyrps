from django.shortcuts import render

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from cmanager.models import Mech
from campaign.models import Campaign

def home(request):
	campaigns = Campaign.objects.order_by('name')
	return render(request, 'campaign/home.html', {
		'campaigns': campaigns
		})

def campaign_detail(request, id):
	campaign = get_object_or_404(Campaign, pk=id)
	return render(request, 'campaign/campaign_detail.html', {
			'campaign': campaign
		})