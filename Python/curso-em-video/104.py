# exercício 104
# função que valida entrada de dados

def validate(msg):
    ok = False
    value = 0 
    while True:
        n = input(msg)
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('Erro! Digite um número inteiro válido!')
        if ok == True: 
            break
    return value

n = validate('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')