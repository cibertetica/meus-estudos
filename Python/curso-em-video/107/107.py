# exercício 107
# programa que faz diversos cálculos com uma quantia de dinheiro informada usando módulos

# programa principal

import calc107

money = float(input('Digite o preço: '))

print(f'A metade de R$ {money:.2f} é R$ {calc107.half(money):.2f}') # metade
print(f'O dobro de R$ {money:.2f} é R$ {calc107.double(money):.2f}') # dobro
print(f'O aumento de 10% em R$ {money:.2f} é R$ {calc107.percent(money):.2f}') # aumento de 10% 