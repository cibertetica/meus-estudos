# exercício 73
# tabela do brasileirão com tuplas
# acessada em 20 de julho de 2019

teams = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético MG', 'Internacional', 'Botafogo',
'Goiás', 'Corinthians', 'Bahia', 'São Paulo', 'Grêmio', 'Atlético PR', 'Fortaleza',
'Ceará', 'Vasco', 'Cruzeiro', 'Fluminense', 'Chapecoense', 'CSA', 'Avaí'
        )

print(f'''
Lista de times do Brasileirão: \n{teams}\n
Os times na G4 (zona de classificação para Libertadores) são: \n{teams[:4]}\n
Os times na Z4 (zona de rebaixamento) são: \n{teams[-4:]}\n 
Times em ordem alfabética: {sorted(teams)}
'''
)
