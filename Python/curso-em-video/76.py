# exercício 76
# listagem de preços com tupla

products = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25
)
for thing in range (0, len(products)):
    if thing % 2 == 0:
        print(f'{products[thing]:<30}') # < alinhado a esquerda 
    else:
        print(f'{products[thing]:>30.2f}') # > alinhado a direita