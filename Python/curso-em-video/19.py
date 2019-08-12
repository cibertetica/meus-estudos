# exercício 19
# escolha aleatória de um nome

from random import choice

one = input('Informe o nome de uma pessoa: ')
two = input('Informe o nome de outra pessoa: ')
three = input('Informe o nome de mais uma pessoa: ')
list = [one, two, three]
print(f'Pessoa escolhida foi: {choice(list)}')