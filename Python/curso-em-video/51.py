# exercício 51
# Programa que lê o primeiro termo e a razão de uma progressão aritmética e mostra os 10 primeiros termos dessa PA.
start = int(input('Informe o primeiro termo: '))
ratio = int(input('Razão: ')) # ratio = número de intervalos
ten = start + (10 - 1) * ratio # fórmula de PA?
for c in range(start, ten + ratio, ratio): 
    print(c)
