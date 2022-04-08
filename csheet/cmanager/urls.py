from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

#from .views import SearchResultsView

app_name = 'cmanager'
urlpatterns = [
	path('', views.home, name='home'),
	path('mech/classes/', views.mech_classes, name='mech_classes'),
	path('mech/<int:id>/', views.mech_detail, name='mech_detail'),
	path('mechs/', views.mechs, name='mechs'),
	path('page/<str:slug>/', views.page, name='page'),
	path('pilots/', views.players, name='players'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
