# exercício 106 
# ajuda interativa para Python
import os
os.system('color')

colors = (
    '\033[0;0m',# 0 - cor padrão
    '\033[1m',  # 1 - negrito
    '\033[32m', # 2 -verde
    '\033[34m', # 3 - azul
    '\033[30m', # 4 - preto
    '\033[37m', # 5 - branco
    '\033[47m', # 6 - fundo branco
    '\033[46m', # 7 - fundo ciano
)

def pyHelpTitle(msg, bg=0, fg=0):
    '''
    msg -> string "Função ou biblioteca: "
    bg -> background color / cor de fundo
    fg - > foreground color / cor de fonte
    '''

    size = len(msg)
    print(colors[bg], colors[fg], '~' * size)
    print(f'{msg}')
    print('~' * size, colors[0])

def pyHelp(command, bg=0, fg=0):
    '''
    command -> comando que será informado para consulta
    bg -> background color / cor de fundo
    fg - > foreground color / cor de fonte
    '''
    while True:
        pyHelpTitle('Py Help | Sistema de ajuda interativa para o Python', 7, 5)
        print(colors[bg], colors[fg])
        com = input(command).strip().lower()
        if com == 'fim':
            break
        else:
            help(com)
    print(colors[0])
        

x = pyHelp('Função ou biblioteca: ', 6, 4)