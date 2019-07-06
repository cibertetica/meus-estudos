# exercício 55
# ler o peso de um grupo de pessoas e indicar quem tem o maior peso e quem tem o menor
high = 0
low = 0
for p in range(1, 6):
    weight = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        high = weight
        low = weight
    else:
        if weight > high:
            high = weight
        if weight < low:
            low = weight

print(f'O maior peso é {high} e o menor peso é {low}.')
            