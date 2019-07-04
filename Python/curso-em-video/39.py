# exercício 39
# idade de alistamento militar

from datetime import date
born_year = int(input('Em que ano você nasceu? '))
age = date.today().year - born_year
print(f'\nVocê tem {age} anos.\n')
if age == 18:
    print('Você está na idade de alistamento militar.')
elif age < 18:
    print('Você ainda é muito jovem para se alistar.')
else:
    print('Você já passou da idade de se alistar.')