from django import forms
from django.db import models
from .models import Contato, SolicitacaoAssociacao
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','assunto','mensagem']
class AssociacaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoAssociacao
        fields = ['nome','email','oab','mensagem']
