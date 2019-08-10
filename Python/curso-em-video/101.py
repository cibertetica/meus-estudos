def voting(year):
    from datetime import date
    current = date.today().year
    age = current - year
    if age < 16:
        return f'Com {age} anos: NÃO VOTA'
    elif 16 <= age < 18 or age >= 65:
        return f'Com {age} anos: VOTO OPCIONAL'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO'

n = int(input('Em que ano você nasceu? '))
print(voting(n))