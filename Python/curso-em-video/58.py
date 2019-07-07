# exercício 58
# Programa em que o computador escolhe um número aleatório de 0 a 10 e o usuário precisa adivinhar qual

from random import randint
print('-' * 5 , 'Jogo da Adivinhação!' , '-' * 5 , '\n')
pc_option = randint(0, 10)
correct = False 
attempts = 0 # quantos palpites a pessoa levou para acertar
while not correct:
    user_option = int(input('Digite um palpite entre 0 a 10: '))
    attempts += 1
    if user_option == pc_option:
        correct = True
    else:
        if user_option < pc_option:
            print('Mais... Tente mais uma vez...')
        else: # elif user_option > pc_option
            print('Menos... Tente mais uma vez...')
print(f'Acertou com {attempts} tentativas!')