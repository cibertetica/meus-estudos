# exercício 99
# função que descobre o maior valor de uma lista

from time import sleep

def higher(*num):
    print(f'Analisando os valores passados...')
    for n in num:
        print(n , end=' ' , flush='True')
        sleep(0.2)
    print(f'\nForam repassados {len(num)} valores.')
    print(f'O maior valor é {max(num)}.')

    # fazendo comparação de valores com um método if

    '''
    c = higher = 0

    if c == 0:
        higher = n
    else:
        if n > higher:
            higher = n
    c += 1 

    '''
    
higher(1,2,3,34,5,87,69,1)