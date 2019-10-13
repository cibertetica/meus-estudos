# CLASSES

class Film():
    def __init__(self, name, year):
        self.name = input(name).title()
        self.year = input(year)

# CODE

listing = []
while True:
    movie = Film('Nome do filme: ', 'Ano de lançamento: ')
    listing.append(f'{movie.name} ({movie.year})')
    while True:
        continue_input = input('Continuar cadastrando filmes? [S/N]: ').upper()[0]
        if continue_input in 'SN':
            break
        print('Opção inválida!')
    if continue_input == 'N':
        break

print('Filmes cadastrados: \n')

for f in listing:
    print(f)

    with open('c:/Users/Martha/OneDrive/Codes/Git/meus-estudos/Python/watchlist-oo/watch.txt', 'a') as saving:
        saving.write(f'{f} \n')