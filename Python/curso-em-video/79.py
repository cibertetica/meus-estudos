# exercício 79
# valores únicos em uma lista

listing = []

while True:
    n = int(input('Digite um número: '))
    if n not in listing:
        listing.append(n)
        print('Valor adicionado com sucesso. ')
    else:
        print('Valor duplicado, não vou adicionar. ')
    
    # continuar digitando números?
    continue_input = input('Quer continuar? [S/N] ').upper().strip()
    while continue_input != 'S' and continue_input != 'N':
        print('Opção inválida!')
        continue_input = input('Quer continuar? [S/N] ').upper().strip()
    if 'N' in continue_input:
        break

print(f'A lista que você criou ficou assim: \n{listing}')