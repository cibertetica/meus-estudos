# exercício 99
# função que descobre o maior valor de uma lista
from time import sleep

def higher(*num):
    print('Analisando os números...')
    for n in num:
        print(n, end=' ', flush='True')
        sleep(0.2)
    c = 0
    higher = num[0] # por padrão, o primeiro número é colocado como o maior    
    while c < len(num) : # laço para comparações
        if num[c] > higher:
            higher = num[c]
        c+= 1
    print(f'\nForam repassados {len(num)} valores')
    print(f'O maior valor é {higher}')

higher(1,2,3,34,5,87,69,1)