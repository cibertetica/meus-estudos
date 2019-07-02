# exercício 28
# jogo da adivinhação

from random import randint

print('Jogo da Adivinhação\n' , '-' * 20)

number = int(input('Digite um número inteiro: '))
choice = randint(0,5)
if number == choice:
    print('Escolha correta! Parabéns!')
else:
    print('Escolha errada! Tente novamente.')