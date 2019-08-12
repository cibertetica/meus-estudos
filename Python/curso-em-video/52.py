# exercício 52
# saber se um número é primo
# crivo de Erastótenes
# fiz bem diferente do proposto no Curso pois dessa forma entendi melhor, pelo menos por enquanto

number = int(input('Informe um número: '))

if number == 1:
    print('O número 1 não é primo pois não tem dois divisores.')
elif number >= 2 and number % 2 == 0:
    print('Números múltiplos de 2 não são números primos.')
elif number >= 3 and number % 3 == 0:
    print('Números múltiplos de 3 não são números primos.')
elif number >= 5 and number % 5 == 0:
    print('Números múltiplos de 5 não são números primos.')
elif number >= 7 and number % 7 == 0:
    print('Números múltiplos de 7 não são números primos.')
else:
    print('Esse número só é divisível por 1 e por ele mesmo, portanto É NÚMERO PRIMO.')