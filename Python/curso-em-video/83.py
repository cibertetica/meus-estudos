# exercício 83
# validando expressões matemáticas

expression = input('Digite a expressão: ')
parentesis = []
for symbol in expression:
    if symbol == '(': # cada vez que for adicionado uma abertura de parênteses, ele coloca nessa lista
        parentesis.append('(')
    elif symbol == ')': # cada vez que for adicionado um fechamento de parênteses, ele coloca nessa lista
        if len(parentesis) > 0: # se a lista tiver itens 
            parentesis.pop() # quando encontra os pares de parêntesis ele deleta tudo, para mostrar que encontrou tudo corretamente
        else: # se a lista não tiver itens
            parentesis.append(')')
            break

if len(parentesis) == 0:
    print('Sua expressão está válida. ')
else:
    print('Sua expressão está incorreta. Verifique a quantidade de parênteses. ')