# exercício 39
# idade de alistamento militar
# coloquei um cálculo para lembrar quando deverá se alistar ou quando deveria ter se alistado

from datetime import date
born_year = int(input('Em que ano você nasceu? '))
age = date.today().year - born_year
print(f'\nVocê tem {age} anos.\n')
if age == 18:
    print('Você está na idade de alistamento militar.')
elif age < 18:
    print('Você ainda é muito jovem para se alistar.')
    print(f'Você deverá se alistar daqui a {18 - age} ano(s).')
else:
    print('Você já passou da idade de se alistar.')
    print(f'Você deveria ter se alistado há {age - 18} ano(s) atrás.')