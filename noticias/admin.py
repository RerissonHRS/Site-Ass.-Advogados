from django.contrib import admin
from .models import Noticia
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','publicado','publicado_em')
    prepopulated_fields = {'slug':('titulo',)}
