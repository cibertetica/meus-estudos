# exercício 59
# programa que faz diversos cálculos

print('-' * 3 , 'Mini calculadora Python' , '-' * 3 , '\n')
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

option = '0'

while option != '5':
    print(
'''
Menu de Opções:
[1] somar
[2] multiplicar
[3] comparação | mostrar o maior valor
[4] mudar números
[5] sair do programa
'''
    )
    option = str(input('Digite o número equivalente a opção desejada: '))
    
    if option == '1':
        print(f'A soma de {n1} e {n2} é {n1 + n2}.')
    elif option == '2':
        print(f'A multiplicação de {n1} e {n2} é {n1 * n2}.')
    elif option == '3':
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os dois valores são iguais.')
    elif option == '4':
        print('Vamos mudar os valores então!\n')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif option == '5':
        print('Finalizando...')
        #exit() -> o laço while já executa essa função de saída automaticamente por causa da sua condição
    else:
        print('Opção inválida! Tente novamente!')
