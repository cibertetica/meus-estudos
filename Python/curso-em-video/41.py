# exercício 41
# análise de categoria de atleta pela idade
from datetime import date
born_year = int(input('Em que ano o atleta nasceu? '))
age = date.today().year - born_year
print(f'\nO atleta tem {age} anos.')

if age < 9:
    print('Atleta MIRIM')
elif age > 9 and age <= 14:
    print('Atleta INFANTIL')
elif age > 14 and age <= 19:
    print('Atleta JÚNIOR')
elif age > 19 and age <=25:
    print('Atleta SÊNIOR')
else: # age > 25
    print('Atleta MASTER')
print(
'''
Classificações: 
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
'''
)
