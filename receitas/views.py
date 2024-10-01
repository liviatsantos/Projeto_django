from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from util.factory import make_receita
from receitas.models import Receita

# Create your views here.
def home(request): 
    receitas = Receita.objects.filter(is_publicado=True).order_by('-id')
    return render(request, 'receitas/pages/home.html', context={
        'receitas' : receitas,
    })

def receita(request, id): 
    receita = Receita.objects.filter(id=id, is_publicado=True).order_by('-id').first()
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': receita,
        'is_detail_page': True,
    })

def categoria(request, categoria_id): 
    receitas = get_list_or_404(Receita.objects.filter(categoria__id=categoria_id, is_publicado=True).order_by('-id'))
    return render(request, 'receitas/pages/categoria.html', context={
        'receitas' : receitas,
        'titulo': f'{receitas[0].categoria.nome} - Categoria'
    })