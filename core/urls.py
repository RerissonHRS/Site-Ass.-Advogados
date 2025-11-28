from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('contato/sucesso/', views.contato_sucesso, name='contato_sucesso'),
    path('associar/', views.associar, name='associar'),
    path('associar/sucesso/', views.associar_sucesso, name='associar_sucesso'),
]
