# exercício 37
# conversor de decimal para binário - octal - hexadecimal

number = int(input('Informe o número a ser convertido: '))
option = input('''Que tipo de conversão deseja fazer?
Digite apenas o número correspondente a opção:
[1] Binário
[2] Octal
[3] Hexadecimal\n'''
)

if option == 1:
    print('Você escolheu conversão para binário ')
    #bin(num)
    print(f'{number} para BINÁRIO é igual a {number:b}. ') # consegui essa info na documentação do python
elif option == 2:
    print('Você escolheu conversão para octal ')
    print(f'{number} para OCTAL é igual a {oct(number)}. ')
elif option == 3:
    print('Você escolheu conversão para hexadecimal ')
    print(f'{number} para HEXADECIMAL é igual a {hex(number)}. ')
elif option != 1 and option != 2 and option != 3:
    print('Opção inválida! Digite seu número e depois as opções [1], [2] ou [3]. ')