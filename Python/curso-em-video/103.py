# exercício 103
# função para apresentar ficha de um jogador

def play(p, g):
    if p.isspace() or p == '': # se o nome do jogador não for informado / for informado espaços ao programa, ele passa o valor desconhecido
        p = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else: 
        g = 0 # se o número de gols não for informado / for informado espaços ao programa, ele passa o valor 0
    return f'O jogador {p} fez {g} gols.'

player = input('Nome do jogador: ').capitalize()
goals = input('Número de gols: ')
print(play(player, goals))