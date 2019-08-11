# exercício 99
# função que descobre o maior valor de uma lista

from time import sleep

def higher(*num):
    print(f'Analisando os números...')
    for n in num:
        print(n , end=' ' , flush='True')
        sleep(0.2)
    print(f'\nForam repassados {len(num)} valores.')
    print(f'O maior valor é {max(num)}.')
    
higher(1,2,3,34,5,87,69,1)