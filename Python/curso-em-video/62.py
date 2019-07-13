# exercício 62
# aprimoração do exercício 61
# Programa que mostra quantas progressões aritméticas o usuário quiser fazer

start = int(input('Informe o primeiro termo: '))
ratio = int(input('Razão: ')) # número de intervalos
term = start # termo
c = 1
total = 0
option = 10
while option != 0:
    total += option # total = total + option
    while c <= total:
        print(f'{term} -> ' , end='')
        term += ratio # total = total + ratio
        c += 1 # c = c + 1
        n_terms = c
    option = int(input('\nQuantos termos você quer mostrar mais? '))
print(f'Progressão finalizada com {n_terms} termos mostrados. ')
print('FIM')