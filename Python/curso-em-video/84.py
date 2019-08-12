# exercício 84
# lista composta e análise de dados

people = []
listing = []
higher_weight = lower_height = 0

while True:
    people.append(input('Nome: ')).capitalize()
    people.append(float(input('Peso: ')))

    if len(listing) == 0: # se a lista está vazia, por padrão o primeiro dado é considerado o maior E menor simultaneamente
        higher_weight = lower_height = people[1]
    else:
        if people[1] < lower_height:
            lower_height = people[1]
        if people[1] > higher_weight:
            higher_weight = people[1]

    listing.append(people[:])
    people.clear()

# tratamento de input     
    while True:
        continue_input = input('Quer continuar? [S/N] ').upper()[0]
        if continue_input in 'SN':
            break
        print('Opção incorreta! Digite apenas S para sim ou N para não.')
    if continue_input == 'N':
        break

print(f'Você cadastrou {len(listing)} pessoas. ')

print(f'O maior peso é de {higher_weight}. ')
for p in listing:
    if p[1] == higher_weight:
        print(f'{p[0]}')
print(f'O menor peso é de {lower_height}. ')

for p in listing:
    if p[1] == lower_height:
        print(f'{p[0]}')