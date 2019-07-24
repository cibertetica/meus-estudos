# exercício 81
# extraindo dados de uma lista

listing = []

while True:
    n = int(input('Digite um valor: '))
    listing.append(n)
# tratamento do input
    continue_input = input('Quer continuar? [S/N] ').upper().strip()
    while continue_input != 'S' and continue_input != 'N':
        print('Opção inválida!')
        continue_input = input('Quer continuar? [S/N] ').upper().strip()
    if continue_input == 'N':
        break

print(f'Você digitou {len(listing)} elementos.')
listing.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listing}.')
if 5 in listing:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')