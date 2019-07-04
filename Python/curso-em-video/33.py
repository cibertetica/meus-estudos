# exercício 33
# ler 3 números e responder qual é o menor
# feito com uma estrutura if

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 < n2 and n1 < n3:
    print(f'O menor valor é {n1}.')
elif n2 < n1 and n2 < n3:
    print(f'O menor valor é {n2}.')
else:
    print(f'O menor valor é {n3}')