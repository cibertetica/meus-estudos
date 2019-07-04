# exercício 38
# ler dois números e analisar qual dos dois é o maior

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Infome o segundo número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2:.2f}.')
elif n2 > n1:
    print(f'{n2} é maior que {n1}. ')
else:
    print('Você digitou duas vezes o mesmo número!')