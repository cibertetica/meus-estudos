# exercício 108
# aprimoração do exercício 107 
# construindo função / módulo para formatação da moeda no formato de real

# programa principal

from calc108 import half, double, increase, decrease
from format108 import real, percent

money = float(input('Informe o preço: R$ '))
increment = int(input('Informe a porcentagem para aumento: '))
discount = int(input('Informe a porcentagem para o desconto: '))

print(f'A metade de {real(money)} é {real(half(money))}') # metade
print(f'O dobro de {real(money)} é {real(double(money))}') # dobro
print(f'O aumento de {percent(increment)} é {real(increase(money, increment))}') # aumento de x%
print(f'O desconto de {percent(discount)} é {real(decrease(money, discount))}') # desconto de x%