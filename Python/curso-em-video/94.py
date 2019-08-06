# exercício 94 
# unindo dicionários e listas

# cada pessoa é armazenada em um dicionário
# cada dicionário é armazenado em uma lista
    # ao final, o programa mostra quantas pessoas foram cadastradas
    # a média de idade
    # uma lista só com as mulheres
    # uma lista com aqueles que tem idade acima da média

person = {} 
people = [] 
sum_age = age_media = 0

while True:
    person.clear() # por padrão esvazia o dicionário

    person['Nome'] = input('Nome: ').title()
    while True:
        person['Gênero'] = input('Gênero: [M/F/O] ').upper()[0]
        if person['Gênero'] in 'MFO': # se o gênero for informado corretamente, sai do loop
            break
        print('Opção inválida! Digite apenas M (masculino), F (feminino) ou O (outro).')

    person['Idade'] = int(input('Idade: '))
    sum_age += person['Idade'] # soma das idades que vão sendo cadastradas

    people.append(person.copy()) # coloca uma cópia do dicionário na lista

    # tratamento de input
    while True: # se o input for informado corretamente, sai do loop
        continue_input = input('Quer continuar? [S/N] ').upper()[0]
        if continue_input in 'SN':
            break
        print('Opção inválida! Digite apenas S ou N.')

    if continue_input == 'N':
        break

age_media = sum_age / len(people) # média das idades

print(f'\n{"Informações":^70}\n')

print(f'Ao todo temos {len(people)} pessoas cadastradas.\n')

print(f'Média de idade: {age_media:.0f}\n')

print(f'Mulheres cadastradas: ')
for p in people:
    if p['Gênero'] == 'F':
        print(f'{p["Nome"]}')

print(f'Idades acima da média: ')
for p in people:
    if p['Idade'] > age_media:
        print(f'{p["Nome"]}')