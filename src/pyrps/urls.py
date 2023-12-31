from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('dnd5/', include('dnd5.urls')),
    path('smb/', include('smb.urls')),
    path('soundboard/', include('soundboard.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)