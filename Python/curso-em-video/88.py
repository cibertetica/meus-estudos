# exercício 88 | Palpites para Mega Sena
# Lembrete de como funciona a Mega Sena:
# jogamos 6 valores, números entre 1 a 60

from random import randint
from time import sleep 

print('-' * 8, 'MEGA SENA', '-' * 8, '\n')
#n_games = int(input('Quantos jogos você quer? '))

games = []
listing = []
g = 1 # total de jogos
n_games = int(input('Quantos jogos você quer? '))
while g <= n_games:
    c = 0
    while True:
        num = randint(1, 60)
        if num not in listing:
            listing.append(num)
            c += 1
        if c >= 6:
            break
    listing.sort() # colocando os números em ordem crescente
    games.append(listing[:])
    listing.clear()
    g += 1

print('\nSorteando....\n')
for i, l in enumerate(games):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')