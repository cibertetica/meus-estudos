#funções

def half(x = 0): # metade
    x = x / 2
    return x

def double(x = 0): # dobro
    x = x * 2
    return x

def increase(x = 0, rate = 0): # aumento de x%
    per = x * (rate / 100)
    x = x + per
    return x

def decrease(x = 0, rate = 0): # desconto de x%
    per = x * (rate / 100)
    x = x - per
    return x
