# cadastro e listagem

listing = []
person = []

def viewData(): # ver os dados cadastrados
    print('Dados já salvos no arquivo: ')
    with open('c:/Users/Martha/OneDrive/Codes/Git/meus-estudos/Python/curso-em-video/115/data.txt' , 'r') as data:
        file = data.read()
        print(file)
    print('Dados digitados recentemente, na fila para serem salvos: ')
    for n, a in listing:
        print(f'{n}: {a} anos')
    print('\n')

    if len(listing) == 0: # se não tiver nada na fila
        print('Você ainda não cadastrou ninguém. \n')
    return listing

def newData(name, age): # novo cadastro
    person.append(input(name).title()) # nome
    while True:
        try:
            person.append(int(input(age))) # idade
            if age > 130:
                print('Idade inválida. Tente novamente.')
        except:
            print('Digite apenas um número inteiro para idade. \n')
        else:
            break
    listing.append(person[:])
    person.clear()
    return name, age

def saveData():
    with open('c:/Users/Martha/OneDrive/Codes/Git/meus-estudos/Python/curso-em-video/115/data.txt' , 'a') as data:
        for n, a in listing:
            data.write(f'{n}: {a} anos\n')