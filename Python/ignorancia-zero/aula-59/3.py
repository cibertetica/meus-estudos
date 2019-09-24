# exercício 3
# crie uma classe Pessoa que modele uma pessoa:
# atributos: nome, idade, peso e altura | métodos: envelhecer, engordar, emagrecer, crescer
# por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm

class Person():
    def __init__(self, name, age, weight, height):
        self.name = input(name)
        try:
            self.age = int(input(age))
            self.weight = float(input(weight))
            self.height = float(input(height))
        except Exception as error:
            print(error)

    def gainWeight(self, gain): # ganhar peso. parâmetro gain especifica quanto o usuário ganhou
        self.weight += float(input(gain))
        print(f'O peso atual de {self.name} é {self.weight}')
    
    def loseWeight(self, lose): # perder peso. parâmetro lose especifica quanto o usuário perdeu
        self.weight += float(input(lose))
        print(f'O peso atual de {self.name} é {self.weight}')

    def gainHeight(self, gain): # crescer. parâmetro lose especifica quanto o usuário cresceu
        self.height += float(input(gain))
        print(f'A altura atual de {self.name} é {self.height}')

    def growUp(self ): # crescer
        self.age += 1
        print(f'Atualizado o cadastro de idade de {self.name}: {self.age} anos.')
        if self.age < 21:
            self.height += 0.5
            print(f'Também atualizamos sua altura, já que cresceu um pouco! {self.height}')
        
