from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('diretoria/', include('diretoria.urls')),
    path('noticias/', include('noticias.urls')),
]
