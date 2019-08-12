# exercício 67
# tabuada com flag

while True:
    n = int(input('Quer ver a tabuada de qual valor?\n[Digite um valor negativo para parar] '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
print('Programa encerrado.')