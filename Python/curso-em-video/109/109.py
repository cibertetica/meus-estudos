# exercício 109
# aprimoração dos exercícios 107-108
# construindo função / módulo para formatação da moeda no formato de real

# programa principal

import calc109
money = float(input('Informe o preço: R$ '))
increment = int(input('Informe a porcentagem para aumento: '))
discount = int(input('Informe a porcentagem para o desconto: '))

print(f'A metade de {calc109.real(money)} é {calc109.half(money)}') # metade
print(f'O dobro de {calc109.real(money)} é {calc109.double(money)}') # dobro
print(f'O aumento de {calc109.percent(increment)} é {calc109.increase(money, increment)}') # aumento de x%
print(f'O desconto de {calc109.percent(discount)} é {calc109.decrease(money, discount)}') # desconto de x%