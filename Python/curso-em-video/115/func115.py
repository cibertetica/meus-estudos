# cadastro e listagem

from time import sleep

listing = []
person = []

def viewData(): # ver os dados cadastrados
    print('Dados já salvos no arquivo: ')
    with open('c:/Users/Martha/OneDrive/Codes/Git/meus-estudos/Python/curso-em-video/115/data.txt' , 'r') as data:
        file = data.read()
        print(file)
    if len(listing) > 0:
        print('Dados digitados recentemente, na fila para serem salvos: ')
        for n, a in listing:
            print(f'{n}: {a} anos')
        print('\n')
    else: # se não tiver nada na fila
        print('Você ainda não cadastrou ninguém. \n')
    return listing

def newData(name, age): # novo cadastro
    person.append(input(name).title()) # nome
    try:
        person.append(int(input(age))) # idade
    except:
        print('Digite apenas um número inteiro para idade. \n')
    listing.append(person[:])
    person.clear()
    return name, age

def saveData():
    if len(listing) > 0:
        with open('c:/Users/Martha/OneDrive/Codes/Git/meus-estudos/Python/curso-em-video/115/data.txt' , 'a') as data:
            for n, a in listing:
                data.write(f'{n}: {a} anos\n')
        print('Salvando...')
        sleep(2)
        print('Dados salvos!\nAté mais! ')
    else:
        print('Você não adicionou nenhum dado dessa vez.')
        print('Até mais!')