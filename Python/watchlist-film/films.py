import csv
from os import system
system('color') # para as cores funcionarem no windows
from time import sleep

watchlist = []

def line():
    print('\033[36m-' * 70 , '\033[0;0m\n')

def newFilm(name):
    new = input(name).title()
    watchlist.append(new)
    return name

def listFilm():
    line()
    print(f'\033[36m{"Lista completa de filmes: ":^70}\033[0;0m\n')
    line()

    print(f'\033[36m{"Filmes previamente salvos: ":^70}\033[0;0m\n')
    line()
    with open('c:/Users/Martha/OneDrive/Codes/Git/meus-estudos/Python/watchlist-film/watch.csv' , 'r') as saved:
        reader = csv.reader(saved)
        for row in reader:
            print([row])

    print(f'\033[36m{"Filmes cadastrados agora: ":^70}\033[0;0m\n')
    line()
    for f in watchlist:
        print(f'{f}')
    line()
    return watchlist

def saveFilm():
    print(f'\033[36m{"Salvando dados...":^70}\033[0;0m\n')
    line()
    sleep(2)
    with open('c:/Users/Martha/OneDrive/Codes/Git/meus-estudos/Python/watchlist-film/watch.csv', 'a') as saving:
        writer = csv.writer(saving, dialect='excel')
        for f in watchlist:
            writer.writerows([f]) # arrumar depois essa MERDA que eu não sei como consertar 
    print(f'\033[36m{"Dados salvos com sucesso! ":^70}\033[0;0m\n')
    line()
    sleep(100)