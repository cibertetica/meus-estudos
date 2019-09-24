# exercício "Quadrado"
# crie uma classe que modele um quadrado
# Atributos: tamanho do lado | Métodos: mudar tamanho do lado, retornar valor do lado e calcular área

class Square():
    def __init__(self):
        self.size = 10
        print('O tamanho padrão dos lados do quadrado é 10.')
    
    def changeSize(self, x):
        self.size = int(input(x))
        #print(f'O tamanho dos lados do quadrado agora é {self.size}.')
        return self.size

    def returnSize(self):
        print(f'O tamanho dos lados do quadrado agora é {self.size}.')
        return self.size

    def area(self):
        area = self.size ** 2
        print(f'A área desse quadrado é {area}.')
        return area

quadrado = Square()
quadrado.changeSize('Que tamanho você quer que os lados do quadrado sejam? ')
quadrado.returnSize()
quadrado.area()