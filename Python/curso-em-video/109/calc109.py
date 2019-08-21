#funções

from format109 import real, percent

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
