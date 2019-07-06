# exercício 54
# ler datas de nascimento de 7 pessoas e apontar quais delas são menores de idade e quais são menores
from datetime import date

current_year = date.today().year
underage = 0
ofage = 0

for c in range(1, 8):
    year = int(input(f'\nEm que ano a {c}ª pessoa nasceu? '))
    age = current_year - year
    print(f'Essa pessoa tem {age} anos.')

    if age >= 18:
        ofage += 1 #ofage = ofage + 1
    else:
        underage += 1 #underage = underage + 1
    
print(f'Temos ao todo {ofage} pessoa(s) maior(es) de idade e {underage} pessoa(s) menor(es) de idade.')