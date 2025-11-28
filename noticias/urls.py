from django.urls import path
from . import views

urlpatterns = [
    # Página de lista de notícias (internas + API TRT9)
    path('', views.lista_noticias, name='noticias_lista'),

    # Página de detalhe de notícia interna (via slug)
    path('<slug:slug>/', views.noticia_detalhe, name='noticia_detalhe'),
]