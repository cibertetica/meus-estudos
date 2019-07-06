# EXERCÍCIO 45
# JOGO DE PEDRA, PAPEL E TESOURA com strings e estrutura if

# lembrete de regras do jogo:
# pedra ganha da tesoura
# tesoura ganha do papel
# papel ganha da pedra

from random import randint # importação do módulo randint que permite ao computador escolher o número aleatoriamente
from time import sleep # pausa no programa antes de fechar sozinho
print('-' * 5, 'JO KEN PO!', '-' * 5)
user_option = int(input( # sua opção
'''
Escolha uma opção:
[1] Pedra
[2] Papel
[3] Tesoura
''')
)
pc_option = randint(1, 3) # opção do computador, seu adversário

if user_option != 1 and user_option != 2 and user_option != 3:
    print('Opção inválida! Digite apenas [1], [2] ou [3] para começar seu jogo. ')

if user_option == 1:
    print('Você escolheu PEDRA!')
elif user_option == 2:
    print('Você escolheu PAPEL!')
else:
    print('Você escolheu TESOURA!')

if pc_option == 1:
    print('O computador escolheu PEDRA!')
elif pc_option == 2:
    print('O computador escolheu PAPEL!')
else:
    print('O computador escolheu TESOURA!')

if user_option == pc_option: # os dois escolhem a mesma opção
    print('EMPATE!')

if pc_option == 1: # PEDRA
    if user_option == 2: # PEDRA x PAPEL
        print('Você ganhou!') 
    elif user_option == 3: # PEDRA x TESOURA
        print('Você perdeu!')

if pc_option == 2: # PAPEL
    if user_option == 1: # PAPEL x PEDRA
        print('Você perdeu!')
    elif user_option == 3: # PAPEL x TESOURA
        print('Você ganhou!')

if pc_option == 3: # TESOURA
    if user_option == 1: # TESOURA x PEDRA
        print('Você perdeu!')
    elif user_option == 2: # TESOURA x PAPEL
        print('Você ganhou!')

sleep(2)
quit()