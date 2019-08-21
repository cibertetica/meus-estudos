# funções para formatação de texto

def real(price = 0, real = 'R$'):
    return f'{real} {price:.2f}'.replace('.' , ',')

def percent(value = 0, symbol = '%'):
    return f'{value}{symbol}'