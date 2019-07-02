# exercício 52
# saber se um número é primo
# crivo de Erastótenes
# fiz bem diferente do proposto no Curso pois dessa forma entendi melhor, pelo menos por enquanto
number = int(input('Informe um número: '))

if number == 1:
    print('O número 1 não é primo pois não tem dois divisores.')
elif number > 2 and number % 2 == 0:
    print('Esse número é maior que 2 e múltiplo de 2, portanto não é número primo.')
elif number > 3 and number % 3 == 0:
    print('Esse número é maior que 3 e múltiplo de 3, portanto não é primo.')
elif number > 5 and number % 5 == 0:
    print('Esse número é maior do que 5 e múltiplo de 5, portanto não é primo.')
elif number > 7 and number % 7 == 0:
    print('Esse número é maior do que 7 e múltiplo de 7, portanto não é primo.')
else:
    print(f'Esse número só é divisível por 1 e por {number}, portanto É NÚMERO PRIMO.')