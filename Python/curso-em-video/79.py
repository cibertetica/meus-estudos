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
    while True:
        continue_input = input('Quer continuar? [S/N] ').upper()[0]
        if continue_input in 'SN':
            break
        print('Opção inválida! Digite apenas S para sim e N para não. ')
    if continue_input == 'N':
        break

print(f'A lista que você criou ficou assim: \n{listing}')