# exercício 8
# conversor de medidas: metro para centímetros e milímetros

value = float(input('Digite um valor em metros a ser convertido: '))

cm = value * 100 # centímetros
mm = value * 1000 # milímetros

# com variáveis
print(f'Em centímetros: {cm:.0f}')
print(f'Em milímetros: {mm:.0f}')