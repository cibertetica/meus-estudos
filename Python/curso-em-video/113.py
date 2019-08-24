# exercício 113
# aprimoração do exercício 104 usando tratamento de erros e exceções

def validateInt(n):
    while True:
        try:
            n = int(input(n))
        except:
            print('Dados inválidos! Tente novamente.')
        else:
            break
    return n
        
def validateFloat(n):
    while True:
        try:
            n = float(input(n))
        except:
            print('Dados inválidos! Tente novamente.')
        else:
            break
    return n

integer = validateInt('Digite um número inteiro: ')
floating = validateFloat('Digite um número real / de ponto flutuante: ')

print(f'Você digitou o número inteiro {integer} e o número real {floating}.')
