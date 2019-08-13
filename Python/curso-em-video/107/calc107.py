#funções

def half(x): # metade
    x = x / 2
    return x

def double(x): # dobro
    x = x * 2
    return x

def increase(x, rate): # aumento de x%
    per = x * (rate / 100)
    x = x + per
    return x

def decrease(x, rate): # desconto de x%
    per = x * (rate / 100)
    x = x - per
    return x