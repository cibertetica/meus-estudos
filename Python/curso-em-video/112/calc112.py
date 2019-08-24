def discount(x=0, y=0, curr='R$'): # x = valor | y = porcentagem
    x = x - (x *  (y / 100))
    return f'{curr} {x:.2f}'.replace('.', ',')
