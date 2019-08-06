# exercício 96 
# função que calcula área de triângulo

def area(x, y):
    z = x * y
    print(f'A área de um terreno {x}m x {y}m é de {z:.1f}m².')


print('Controle de Terrenos\n')
width = float(input('Largura (m): '))
height = float(input('Comprimento (m): '))

area(width, height)