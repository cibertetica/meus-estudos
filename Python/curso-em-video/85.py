# exercício 85 
# lista composta -> lista com pares e ímpares

listing = [[], []] # posição 0 = pares | posição 1 = ímpares

for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    c += 1

    if num % 2 == 0:
        listing[0].append(num)
    else:
        listing[1].append(num)

print(f'Lista: \nNúmeros pares: {listing[0]}\nNúmeros ímpares: {listing[1]}')