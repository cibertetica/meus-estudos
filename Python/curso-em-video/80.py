# exercício 80
# lista ordenada sem repetições e sem o uso do método sort()

listing = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > listing[-1]: # listing na última posição | se o número for maior do que o número que está no último elemento
        listing.append(n)
        print(f'O valor {n} foi armazenado no fim da lista. ')
    else:
        position = 0
        while position < len(listing): # vai da posição 0 até a última posição
            if n <= listing[position]:
                listing.insert(position, n)
                print(f'O valor {n} foi armazenado na posição {position}.')
                break
            position += 1

print(f'Os valores digitados em ordem foram: {listing}')