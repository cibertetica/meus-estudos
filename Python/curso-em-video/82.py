# exercício 82
# separando valores pares de ímpares em uma lista

listing = []
even = [] # lista de pares
odd = [] # lista de ímpares

while True:
    listing.append(int(input('Digite um valor: ')))

# tratamento do input
    continue_input = input('Quer continuar? [S/N] ').upper().strip()
    while continue_input != 'S' and continue_input != 'N':
        print('Opção inválida!')
        continue_input = input('Quer continuar? [S/N] ').upper().strip()
    if continue_input == 'N':
        break

for index, value in enumerate(listing):
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

print(f'A lista completa que você criou é {listing}')
print(f'A lista dos números pares é {even}')
print(f'A lista dos números ímpares é {odd}')