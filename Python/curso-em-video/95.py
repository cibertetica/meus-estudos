# exercício 95
# aprimoração do exercício 93

# exercício 93
# cadastro de jogador de futebol utilizando dicionários

player = {}
team = []
goals = []

while True:
    player.clear() # limpa o dicionário
    goals.clear() # limpa a lista de gols

    player['nome'] = input('Nome do jogador: ').capitalize() # nome do jogador fica formatado com a primeira letra maiúscula
    player['partidas'] = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    for m in range(0, player['partidas']):
        goals.append(int(input(f'\tQuantos gols na partida {m + 1}? ')))
    player['gols'] = goals[:] # copia a lista goals para o espaço gols no dicionário
    player['total'] = sum(goals) # copia a soma da lista goals para o espaço gols no dicionário

    team.append(player.copy()) # copia todo o dicionário para a lista team

    while True:
        continue_input = input('Cadastrar mais jogadores? [S/N] ').upper()[0] # letra maiúscula | usa apenas o primeiro caractere
        if continue_input in 'SN':
            break
        print('Opção inválida! Digite apenas S para Sim ou N para Não.')

    if continue_input == 'N':
        break

print(f'{"cod.":<5}', end=' ')
for k in player.keys():
    print(f'{k:<15}', end=' ')
print()

for i, p in enumerate(team):
    print(f'{i:<5}', end=' ')
    for p in player.values():
        print(f'{str(p):<15}', end=' ') # é necessário um typecast para que a formatação reconheça a variável-valor
print()

while True:
    option = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if option == 999:
        break
    if option >= len(team):
        print('Não existe jogador cadastrado nesse número. Tente novamente.')
    else:
        print(f'Levantamento do jogador {team[option]["nome"]}:')
        for i, g in enumerate(team[option]['gols']):
            print(f'Na partida {i + 1}, fez {g} gols.')
        