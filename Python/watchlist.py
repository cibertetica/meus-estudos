import csv

print(f' {"Lista de filmes para assistir! ":^70} ')
print(f' {"Digite 999 para parar. ":^70} ')

watchlist = []

while True:
    film = input('\nNome do filme: ').title()
    
    if film == '999':
        break

    watchlist.append(film)
    
print(f' {"Lista completa de filmes: ":^70} \n')

for f in watchlist:
    print(f'{f}')

with open('watch.csv', 'w') as csvfile:
     writer = csv.writer(csvfile, dialect='excel')
     writer.writerows(watchlist)