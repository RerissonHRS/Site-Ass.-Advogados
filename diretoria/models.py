from django.db import models

class Membro(models.Model):
    nome = models.CharField(max_length=140)
    cargo = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='membros/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordem', 'nome']  # Ordenação automática

    def __str__(self):
        return self.nome

