from django.shortcuts import render, redirect
from .models import AreaAtuacao
from .forms import ContatoForm, AssociacaoForm

# Importações para exibir diretoria e notícias na Home
from diretoria.models import Membro
from noticias.models import Noticia


def home(request):
    # Busca até 6 áreas de atuação
    areas = AreaAtuacao.objects.all()[:6]

    # Busca 3 membros da diretoria para aparecer na Home
    membros_preview = Membro.objects.all()[:3]

    # Busca 3 notícias mais recentes
    noticias_preview = Noticia.objects.order_by('-publicado_em')[:3]

    return render(request, 'core/home.html', {
        'areas': areas,
        'membros_preview': membros_preview,
        'noticias_preview': noticias_preview,
    })


def sobre(request):
    return render(request, 'core/sobre.html')


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()  # salva no banco
            return redirect('contato_sucesso')
    else:
        form = ContatoForm()

    return render(request, 'core/contato.html', {'form': form})


def contato_sucesso(request):
    return render(request, 'core/contato_sucesso.html')


def associar(request):
    if request.method == 'POST':
        form = AssociacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('associar_sucesso')
    else:
        form = AssociacaoForm()

    return render(request, 'core/associar.html', {'form': form})


def associar_sucesso(request):
    return render(request, 'core/associar_sucesso.html')

