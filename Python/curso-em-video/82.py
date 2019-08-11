# exercício 82
# separando valores pares de ímpares em uma lista

listing = []
even = [] # lista de pares
odd = [] # lista de ímpares

while True:
    listing.append(int(input('Digite um valor: ')))

# tratamento do input
    while True: 
        continue_input = input('Quer continuar? [S/N] ').upper()[0] # letra maiúscula | pega só a primeira letra digitada
        if continue_input in 'SN':
            break
        print('Opção inválida! Digite apenas S para sim ou N para não.')
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