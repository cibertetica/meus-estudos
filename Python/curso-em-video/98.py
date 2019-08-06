# exercício 98
# função de contador

from time import sleep

def counter(x, y, z): # x -> início | y -> fim | z -> intervalo

    if z < 0:
        z *= -1 # se o intervalo digitado pelo usuário for um número negativo, transforma em um número positivo para evitar erros de loop infinito
    
    print(f'Contando de {x} a {y} com intervalo de {z} em {z}.')
    
    c = x
    if x > z:
        while c >= y:
            print(c , end=' ' , flush=True) # flush=True -> não liga buffer de tela
            sleep(0.5)
            c -= z
        print('\nFim!\n')
    else:
        while c <= y:
            print(c , end=' ' , flush=True)
            sleep(0.5)
            c += z
        print('\nFim!\n')


counter(1, 10, 1)
counter(10, 1, 1)

print('Agora é a sua vez de personalizar a contagem!\n')
num1 = int(input('Início: '))
num2 = int(input('Fim: '))
step = int(input('Intervalo: '))

counter(num1, num2, step)