from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_membros, name='diretoria_lista'),
    path('<int:pk>/', views.membro_detalhe, name='membro_detalhe'),
]
