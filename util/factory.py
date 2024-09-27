from random import randint
from faker import Faker

fake = Faker('pt_BR')

def rand_ratio():
    return randint(840, 900), randint(473, 573)

def make_receita():
    return {
        'id' : fake.random_number(digits=2, fix_len=True),
        'titulo' : fake.sentence(nb_words=6),
        'descricao' : fake.sentence(nb_words=12),
        'tempo_preparacao' : fake.random_number(digits=2, fix_len=True),
        'tempo_preparacao_unidade' : 'Minutos',
        'porcoes' : fake.random_number(digits=2, fix_len=True),
        'porcoes_unidade' : 'Porções',
        'modo_preparacao' : fake.text(2000),
        'data_criacao' : fake.date_time(),
        'autor' : {
            'primeiro_nome' : fake.first_name(), 
            'ultimo_nome' : fake.last_name(), 
        },
        'categoria' : {
            'nome' : fake.word()
        },
        'capa' : {
            'url' : 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

