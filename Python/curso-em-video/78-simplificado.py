# exercício 78 simplificado
# maior e menor valores com listas usando max e min

listing = []

for c in range(0, 5):
    listing.append(int(input(f'Digite um valor para a posição {c + 1}: ')))

print(f'Os números informados foram {listing}')
print(f'O maior valor é {max(listing)}, que está na posição {listing.index(max(listing)) + 1}')
print(f'O menor valor é {min(listing)}, que está na posição {listing.index(min(listing)) + 1}')