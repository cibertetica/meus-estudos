# exercício 50
# somar 6 números informados pelo usuário

s = 0
for c in range(1, 7):
    n = int(input('Informe um número inteiro: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos valores é {s}')