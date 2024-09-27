from django.shortcuts import render
from django.http import HttpResponse
from util.factory import make_receita

# Create your views here.
def home(request): 
    return render(request, 'receitas/pages/home.html', context={
        'receitas' : [make_receita for _ in range(5)],
    })

def receita(request, id): 
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': make_receita(),
        'is_detail_page': True,
    })