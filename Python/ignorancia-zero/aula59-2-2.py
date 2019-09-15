# exercício "Retângulo"
# pessoa informa um local e usando a classe retângulo o programa deve calcular quantos retângulos são necessários para fazer o piso

class Rect():
    def __init__(self):
        self.width = 10
        self.height = 5
        print(f'O tamanho padrão da base é {self.width}.')
        print(f'O tamanho padrão da altura é {self.height}.')

    def change(self, x, y):
        self.width = int(input(x))
        self.height = int(input(y))

    def returnSize(self):
        print(f'O tamanho da base é {self.width} e da altura é {self.height}.')
        return self.width, self.height

    def area(self):
        area = self.width * self.height
        print(f'A área do retângulo é {area}.')
        return area

    def perimeter(self):
        per = (self.width * 2) + (self.height * 2) 
        print(f'O perímetro do retângulo é {per}.')
        return per

retangulo = Rect()
retangulo.change('Informe o tamanho da base: ', 'Informe o tamanho da altura: ')
retangulo.returnSize()
retangulo.area()
retangulo.perimeter()