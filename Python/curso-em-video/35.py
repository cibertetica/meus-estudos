# exercício 35
# ver exercício 42 depois
# um lado de um triângulo não pode ser maior que a soma dos outros dois lados

print('ANALISADOR DE TRIÂNGULOS')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < (r2 + r3) and r2 < (r1 + r2) and r3 < (r1 + r2):
    print('É possível fazer um triângulo.')
else:
    print('Não é possível fazer um triângulo.')