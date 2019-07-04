# exercício 42
# aprimoração do exercício 35 sobre triângulos

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('É possível fazer um triângulo.')
    if r1 == r2 == r3:
        print('É um triângulo equilátero.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('É um triângulo escaleno.')
    else:
        print('É um triângulo isósceles')
else:
    print('Não é possível fazer um triângulo.')