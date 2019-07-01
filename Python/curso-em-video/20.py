# exercício 20 
# sorteio aleatório de ordem de nomes de alunos

from random import shuffle
print('---' * 11)
print('Informe os dados pedidos a seguir.')
print('---' * 11)
n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')
n4 = input('Nome do aluno 4: ')
list = [n1, n2, n3, n4]
shuffle(list)
print(f''''
A ordem de apresentação será... 
{list}
''')