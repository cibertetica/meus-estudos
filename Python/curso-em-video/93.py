# exercício 93
# cadastro de jogador de futebol utilizando dicionários

player = {}

player["nome"] = input('Nome do jogador: ').title()
player["partidas"] = int(input(f'Quantas partidas {player["nome"]} jogou? '))
goals = []

for m in range(0, player['partidas']):
    goals.append(int(input(f'\tQuantos gols na partida {m + 1}? ')))

player["gols"] = goals

print('Dados armazenados com sucesso! \n')

for k, v in player.items():
    print(f'\t{k} - > {v}')

print('\nInformações detalhadas:\n')
print(f'O jogador {player["nome"]} jogou {player["partidas"]} partidas.')

for m, g in enumerate(goals):
    print(f'\tNa partida {m + 1}, fez {g} gols.')

print(f'\nFez um total de {sum(goals)} gols.')

