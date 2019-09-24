# exercício 11
# ler a largura e altura de uma parede em metros. calcular sua área e a quantidade de tinta necessária para pintar.
# cada 1l de tinta pinta uma área de 2m²

width = float(input('Informe a largura da parede: ')) # width = largura
height = float(input('Informe a altura da parede: ')) # height = altura
area = width * height # fórmula de área = largura * altura
print(f'Sua parede tem dimensão de {width:.1f}m x {height:.1f}m. A área é de {area:.1f}m². ')
ink = area / 2 # ink = tinta
print(f'Para pintar esse espaço, você precisará de {ink:.1f}l de tinta. ')

