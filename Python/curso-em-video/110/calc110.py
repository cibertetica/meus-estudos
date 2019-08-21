#funções

from format110 import real, percent

def half(x = 0, formating=True): # metade | x -> valor monetário | formatação para real sempre ativa
    x = x / 2
    return x if formating == False else real(x)

def double(x = 0, formating=True): # dobro | x -> valor monetário | formatação para real sempre ativa
    x = x * 2
    return x if formating == False else real(x)

def increase(x = 0, rate = 0, formating=True): # aumento de x% | x -> valor monetário | formatação para real sempre ativa
    per = x * (rate / 100)
    x = x + per
    return x if formating == False else real(x)

def decrease(x = 0, rate = 0, formating=True): # desconto de x% | x -> valor monetário | formatação para real sempre ativa
    per = x * (rate / 100)
    x = x - per
    return x if formating == False else real(x)

def resume(x = 0, more = 0, less = 0): # resumo de todos as funções que serão feitas | x -> valor monetário | more -> porcentagem de aumento | less -> porcentagem de desconto
    print('-' * 30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)
    print(f'Preço analisado: {real(x)}')
    print(f'Metade do preço: {half(x)}')
    print(f'Dobro do preço: {double(x)}')
    print(f'{percent(more)} de aumento: {increase(x)}')
    print(f'{percent(less)} de aumento: {decrease(x)}')