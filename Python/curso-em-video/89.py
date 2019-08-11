# exercício 89 
# boletim com listas compostas

listing = []

while True:
    name = input('Nome: ').title()
    note1 = float(input('Nota 1: '))
    note2 = float(input('Nota 2: '))
    average = (note1 + note2) / 2

    listing.append([name, [note1, note2], average])

    # tratamento de input
    while True:
        analysis = input('Quer continuar? [S/N] ').upper()[0]
        if analysis in 'SN':
            break
        print('Opção inválida! Digite apenas S para sim ou N para não')

    if analysis == 'N':
        break
    
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":<10}\n')

for i, a in enumerate(listing):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}\n')

while True:
    detail = int(input('Deseja ver as notas de algum aluno?\nNão: Digite 999\nSim: Digite o número do aluno '))
    if detail == 999:
        print('Finalizando...')
        break
    if detail <= len(listing) - 1:
        print(f'Notas de {listing[detail][0]} são {listing[detail][1]}')