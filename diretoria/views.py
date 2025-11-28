from django.shortcuts import render, get_object_or_404
from .models import Membro
def lista_membros(request):
    membros = Membro.objects.filter(ativo=True).order_by('ordem')
    return render(request, 'diretoria/lista.html', {'membros': membros})
def membro_detalhe(request, pk):
    membro = get_object_or_404(Membro, pk=pk)
    return render(request, 'diretoria/detalhe.html', {'membro': membro})
