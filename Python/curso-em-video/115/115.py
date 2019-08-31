# exercício 115
# criar um sistema de armazenamento de dados simples que armazena as informações digitadas pela pessoa em um arquivo .txt
# informações a serem cadastradas = nome e idade

import func115
from time import sleep
from os import system
system('color') # módulo para colocar cores no programa no Windows

def menu():
    print('-' * 40)
    print(f'\033[36m{"Menu Principal":^40}\033[0;0m')
    print('-' * 40)

    print('\033[36m 1 - \033[0;0m Ver pessoas cadastradas')
    print('\033[36m 2 - \033[0;0m Cadastrar nova pessoa')
    print('\033[36m 3 - \033[0;0m Salvar e sair')

def opTreat(op):
    try:
        user_input = int(input(op))
    except:
        print('Opção inválida! Tente novamente.')
    else:
        if user_input > 3:
            print('Esse programa só tem duas opções. Tente novamente.')
        elif user_input == 1:
            func115.viewData()
        elif user_input == 2:
            name = ('Nome: ')
            age = ('Idade: ')
            func115.newData(name, age)
        elif user_input == 3:
            func115.saveData()
            print('Salvando...')
            sleep(2)
            print('Dados salvos!\nAté mais! ')
            exit()

while True:
    menu()
    option = ('Sua opção: ')
    opTreat(option)
    if option == 3:
        break
