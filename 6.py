# exercício 6
# dobro, triplo e raiz quadrada
from math import sqrt

n = float(input('Digite um número: '))
double = n * 2
triple = n * 3
squareroot = sqrt(n)
# ou
# squareroot2 = n ** 1/2

print(f'Dobro: {double}')
# sem variável:
# print(f'Dobro: {n * 2}')
print(f'Triplo: {triple}')
# sem variável:
# print(f'Triplo: {n * 3}')
print(f'Raiz quadrada: {squareroot:.2f}')
# sem variável:
# print(f'Raiz quadrada: {sqrt(n)}')
# sem usar biblioteca
# print(f'Raiz quadrada: {squareroot2:.2f}')
# sem usar biblioteca e sem usar variável
# print(f'Raiz quadrada usando método aritmético: {n ** (1/2)}')