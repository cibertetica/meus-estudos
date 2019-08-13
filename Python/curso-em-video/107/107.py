# exercício 107
# programa que faz diversos cálculos com uma quantia de dinheiro informada usando módulos

# programa principal

import calc107

money = float(input('Informe o preço: R$ '))
increment = int(input('Informe a porcentagem para aumento: '))
discount = int(input('Informe a porcentagem para o desconto: '))

print(f'A metade de R$ {money:.2f} é R$ {calc107.half(money):.2f}') # metade
print(f'O dobro de R$ {money:.2f} é R$ {calc107.double(money):.2f}') # dobro
print(f'O aumento de {increment}% é R$ {calc107.increase(money, increment):.2f}') # aumento de x%
print(f'O desconto de {discount}% é R$ {calc107.decrease(money, discount):.2f}') # desconto de x%