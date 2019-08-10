# exercício 102
# função para calcular fatorial de um número através de estrutura de repetição

def fact(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f'O fatorial de {n} é {f}.'

x = int(input('Número para calcular o fatorial: '))
print(f'{fact(x)}')