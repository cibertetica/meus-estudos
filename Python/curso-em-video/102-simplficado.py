# exercício 102 
# função para calcular fatorial de um número usando a biblioteca math

def fact(x):
    from math import factorial 
    print(f'O fatorial de {x} é {factorial(x)}.')

n = int(input('Número que quer saber o fatorial: '))
fact(n)