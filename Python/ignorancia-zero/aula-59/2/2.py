# exercício "Retângulo"
# pessoa informa um local e usando a classe retângulo o programa deve calcular quantos retângulos são necessários para fazer o piso

import classe

place = classe.Rect()
place.change('Informe o comprimento do local: ', 'Informe a largura do local: ')
place_area = place.area()

floor = classe.Rect()
floor.change('Informe o comprimento do piso: ', 'Informe a largura do piso: ')
floor_area = floor.area()

total = round(place_area / floor_area)
print(f'Serão necessários {total} pisos para cobrir o espaço de {place_area}m²')