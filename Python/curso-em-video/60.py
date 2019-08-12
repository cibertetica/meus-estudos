# exercício 60
# cálculo de fatorial com passo a passo

n = int(input('Digite o número que quer calcular o fatorial: '))
c = n # faz com que o contador tenha o mesmo valor de n
f = 1 # fator nulo de multiplicação

print(f'Calculando {n}!')

while c > 0:
    print(f'{c}' , end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c # cálculo do fatorial | f = f * c
    c -= 1 # c = c - 1
print(f)