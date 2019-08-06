''# exercício 92
# cadastro de trabalhador utilizando dicionários
from datetime import date

database = {}

database['Nome'] = input('Nome: ').title()
year = int(input('Ano de nascimento:  '))
database['Idade'] = date.today().year - year
database['CTPS'] = int(input('Carteira de trabalho: [Digite 0 se não tiver] '))
if database['CTPS'] != 0:
    database['Contratação'] = int(input('Ano de contratação: '))
    database['Salário'] = float(input('Salário: R$ '))
    database['Aposentadoria'] = database['Idade'] + ((database['Contratação'] + 35) - date.today().year)

print('\tDados cadastrados com sucesso!\n')
for k, v in database.items(): # key, value
    print(f'\t{k} -> {v}')
''