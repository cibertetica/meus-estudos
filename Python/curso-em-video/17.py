# exercício 17
# calcular a hipotenusa de um triângulo

from math import hypot 

oposite = float(input('Informe o valor do cateto oposto: ')) # valor do cateto oposto do triângulo
adjacent = float(input('Informe o valor do cateto adjacente: ')) # valor do cateto adjacente do triângulo
hipo = hypot(oposite, adjacent)
'''
# forma matemática: 
# o quadrado da hipotenusa é igual a soma dos quadrados dos catetos
hipo = (oposite ** 2 + adjacent ** 2) ** (1/2)
'''
print(f'A hipotenusa desse triângulo é {hipo:.1f} ')
