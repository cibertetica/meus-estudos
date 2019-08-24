def real(msg): # msg = input
    valid = False
    while not valid:
        enter = str(input(msg)).replace(',' , '.')
        if enter.isalpha():
            print(f'Erro! {enter} é um preço inválido! ')
        else:
            valid = True
            return float(enter)