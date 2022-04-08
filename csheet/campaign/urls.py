from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

#from .views import SearchResultsView

app_name = 'campaign'
urlpatterns = [
	path('', views.home, name='home'),
	path('campaign/<int:id>/', views.campaign_detail, name='campaign_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
