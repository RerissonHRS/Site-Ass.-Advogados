from django.db import models
class AreaAtuacao(models.Model):
    titulo = models.CharField(max_length=120)
    resumo = models.TextField(blank=True)
    icone = models.CharField(max_length=64, blank=True)
    def __str__(self):
        return self.titulo
class Contato(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nome} - {self.assunto}"
class SolicitacaoAssociacao(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    oab = models.CharField(max_length=30, blank=True)
    mensagem = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Solicitação: {self.nome}"
