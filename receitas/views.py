from django.shortcuts import render
from django.http import HttpResponse
from util.factory import make_receita
from receitas.models import Receita

# Create your views here.
def home(request): 
    receitas = Receita.objects.filter(is_publicado = True).order_by('-id')
    return render(request, 'receitas/pages/home.html', context={
        'receitas' : receitas,
    })

def receita(request, id): 
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': make_receita(),
        'is_detail_page': True,
    })

def categoria(request, categoria_id): 
    receitas = Receita.objects.filter(categoria__id=categoria_id, is_publicado=True).order_by('-id')
    return render(request, 'receitas/pages/categoria.html', context={
        'receitas' : receitas,
    })