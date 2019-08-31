import films

films.line()
print(f'\033[36m{"Lista de filmes para assistir ":^70}\033[0;0m\n')
films.line()

while True:
    films.newFilm('Nome do filme: ')

    while True:
        continue_input = input('Continuar adicionando filmes? [S/N] ').upper()[0]
        if continue_input in 'SN':
            break
        print('\033[31mOpção inválida! Tente novamente.\033[0;0')
    if continue_input == 'N':
        break

films.listFilm()
films.saveFilm()