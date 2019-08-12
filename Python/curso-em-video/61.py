# exercício 61
# exercício 51 refeito com estrutura while
# Programa que lê o primeiro termo e a razão de uma progressão aritmética e mostra os 10 primeiros termos dessa PA

start = int(input('Informe o primeiro termo: '))
ratio = int(input('Razão: ')) # número de intervalos
ten = start # termo
c = 1

while c <= 10:
    print(f'{ten} -> ' , end='')
    ten += ratio # ten = ten + ratio
    c += 1 # c = c + 1
print('FIM')