import feedparser
from django.shortcuts import render, get_object_or_404
from .models import Noticia


def lista_noticias(request):
    # --------------------------
    # NOTÍCIAS INTERNAS (se quiser manter)
    # --------------------------
    internas = Noticia.objects.filter(publicado=True).order_by('-publicado_em')

    # --------------------------
    # NOTÍCIAS EXTERNAS (Google News RSS)
    # --------------------------
    url_rss = "https://news.google.com/rss/search?q=notícias+jurídicas&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    noticias_api = []
    try:
        feed = feedparser.parse(url_rss)
        for entry in feed.entries[:10]:  # pega as 10 primeiras
            noticias_api.append({
                "titulo": entry.title,
                "resumo": entry.summary if hasattr(entry, "summary") else "Sem resumo disponível",
                "publicado_em": entry.published if hasattr(entry, "published") else "",
                "link": entry.link,
                "api": True
            })
    except Exception as e:
        print("Erro ao consultar Google News RSS:", e)

    # --------------------------
    # COMBINAR NOTÍCIAS (internas + externas)
    # --------------------------
    noticias_combinadas = list(internas) + noticias_api

    return render(request, 'noticias/lista.html', {
        'noticias': noticias_combinadas
    })


def noticia_detalhe(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})
