# exercício 100 
# funções para sortear e somar números

from random import randint
from time import sleep

def randomize(listing):
    for c in range(0, 5):
        n = randint(1, 5)
        listing.append(n)
        c += 1

    print('\nOs valores sorteados foram: ')

    for n in listing:
        print(n, end=' ', flush=True)
        sleep(0.5)

def listsum(listing):
    evensum = 0
    print(f'\nOs elementos pares na lista são: ')
    for n in listing:
        if n % 2 == 0:
            print(n, end=' ', flush=True)
            sleep(0.5)
            evensum += n
    print(f'\nA soma dos elementos pares da lista é:\n{evensum}')

num = []
randomize(num)
listsum(num)