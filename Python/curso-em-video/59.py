# exercício 59
# programa que faz diversos cálculos
'''
EM CONSTRUÇÃO
print('-' * 3 , 'Mini calculadora Python' , '-' * 3)
option = 0
while option != 5:
    option = int(input('Escolha uma opção:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\n'))
    if option == 1:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(f'A soma desses valores é {n1 + n2}.') # não quis criar mais uma variável aqui pra não ocupar muita memória
    elif option == 2:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(f'A multiplicação desses valores é {n1 * n2}.')
    elif option == 3:
        n1 = float('Digite o primeiro número para a comparação: ')
        n2 = float('Digite o segundo número para a comparação: ')
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 < n2:
            print(f'{n1} é menor que {n2}')
        else:
            print('Dois números iguais.')
    elif option == 4:
'''