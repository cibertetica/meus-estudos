# exercício 68
# jogo de par ou ímpar elaborado

from random import randint

game_amount = user_win = 0 # game_amount -> quantas vezes a pessoa joga | user_win -> quantas vezes a pessoa ganha 

while True:
    print('\nVamos jogar par ou ímpar!\n')
    user = int(input('Informe um número de 0 a 5: ')) # número jogado pelo usuário
    pc = randint(0, 5) # número jogado pelo computador
    while user > 5: # se a pessoa insiste em colocar um número maior que 5...
        print('Opção inválida!')
        user = int(input('Informe um número de 0 a 5: '))

    # pessoa escolhe par ou ímpar?
    odd_even_user = input('Par ou Ímpar? [P/I] ').upper().strip()[0] # letra maiúscula -> ignora espaços -> ignora depois do primeiro caractere
    # se a pessoa escolhe um, o computador escolhe o contrário, é claro
    if odd_even_user == 'P':
        odd_even_pc = 'I'
    else:
        odd_even_pc = 'P'
    # se a pessoa digitar errado, o computador tem que a forçar a digitar certo...
    while odd_even_user != 'P' and odd_even_user != 'I':
        print('Opção inválida!')
        odd_even_user = input('Digite apenas P para Par ou I para Ímpar: ').upper().strip()[0]

    total = user + pc # soma dos valores

    # resultado do jogo com informações completas.
    print(f'''
    Você escolheu o número {user} e a opção {odd_even_user}.
    O computador escolheu o número {pc} e a opção {odd_even_pc}.
    A soma dos números é {total}.
    '''
    )
    if total % 2 == 0:
        result = 'P'
        print(f'{total} é um número par.')
    else:
        result = 'I'
        print(f'{total} é um número ímpar')

    if odd_even_user == result:
        print('Você ganhou!')
        user_win += 1
    else:
        print('Você perdeu!')
    game_amount += 1
    
    #continuar o jogo?
    continue_game = input('Quer continuar jogando? [S/N] ').upper().strip()[0]
    while continue_game != 'S' and continue_game != 'N':
        print('Opção inválida!')
        continue_game = input('Quer continuar jogando? [S/N] ').upper().strip()[0]
    if continue_game == 'N':
        break

print('Fim de jogo!')
print(f'Você jogou {game_amount} vezes e ganhou {user_win} vezes!')