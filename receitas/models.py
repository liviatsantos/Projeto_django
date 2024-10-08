from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=65)
    decricao = models.CharField(max_length=165)
    slug = models.SlugField()
    tempo_preparacao = models.IntegerField()
    tempo_preparacao_unidade = models.CharField(max_length=12)
    porcoes = models.IntegerField()
    porcoes_unidade = models.CharField(max_length=12)
    modo_preparacao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    is_publicado = models.BooleanField(default=False)
    capa = models.ImageField(upload_to='receita/capa/%Y/%m/%d/', blank=True, default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo