# exercício 1:
# Faça um programa completo usando funções e classes que:
#       - classe Ponto, atributos x e y
#       - classe Retangulo, atributos altura e largura
#       - função para imprimir os valores da classe Ponto
#       - função para encontrar o centro de um Retangulo 
# Ao criar objetos da classe Retangulo, cada um deles deve ter um vértice de partida, esses vértices são objetos da classe Ponto

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x = {self.x} | y = {self.y}')

class Retangulo():
    def __init__(self, width, height, x, y): # largura e altura respectivamente
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def centro(self):
        centro = (self.x + self.y) / 2
        print(f'O centro do retângulo é {centro}')

ponto = Ponto(1, 5)
ret = Retangulo(30, 20, ponto, ponto)
ret.centro()