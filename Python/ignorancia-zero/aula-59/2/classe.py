# exercício "Retângulo"
# crie uma classe que modele um retângulo. 
# Atributos: tamanho da base, tamanho da altura
# Métodos: Mudar valor dos lados, retornar valor dos lados, calcular área e calcular perímetro

class Rect():
    
    def change(self, x, y):
        self.width = int(input(x))
        self.height = int(input(y))

    def returnSize(self):
        print(f'O tamanho agora é {self.width} x {self.height}.')
        return self.width, self.height

    def area(self):
        area = self.width * self.height
        print(f'A área é {area}m².')
        return area

    def perimeter(self):
        per = (self.width * 2) + (self.height * 2) 
        print(f'O perímetro é {per}m.')
        return per