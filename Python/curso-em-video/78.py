# exercício 78
# maior e menor valores com listas

listing = []

for c in range(0, 5):
    listing.append(int(input(f'Digite um valor para a posição {c + 1}: ')))

higher = lower = listing[0] # por padrão, o primeiro elemento é tanto o maior como o menor

c = 0
while c < len(listing):
    if listing[c] > higher:
        higher = listing[c]
    if listing[c] < lower:
        lower = listing[c]
    c += 1

print(f'Os números informados foram {listing}')
print(f'O maior valor da lista é {higher}, que está na posição {listing.index(higher) + 1}')
print(f'O menor valor da lista é {lower} que está na posição {listing.index(lower) + 1}')