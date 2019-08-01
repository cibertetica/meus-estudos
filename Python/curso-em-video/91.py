# exercício 91
# jogo de dados

from random import randint
from time import sleep
from operator import itemgetter

print('-' * 5 , 'Jogo de dados' , '-' * 5, '\n')

game = {
'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6),
}
ranking = []

for k, v in game.items():
    print(f'{k:^16}-> {v}')
    sleep(1)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True) # ordena o dicionário pelos valores do números aleatórios

print()
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar -> {v[0]} com {v[1]}')
