# exercício 105 
# função que gera dicionário com total, média, nota maior e menor através de um número ilimitado de notas

def funcNotes(*num, sit=False):
    notes = {}
    total = c = 0
    higher = lower = num[0] # por padrão, o maior e menor valor simultaneamente é o primeiro
    
    while c < len(num): 
        total += num[c] # somar todos os valores

        if num[c] >= higher: # comparação para encontrar algum valor maior que o já atribuído
            higher = num[c] 

        if num[c] <= lower: # comparação para encontrar algum valor menor que o já atribuído
            lower = num[c]

        c+= 1

    # atribuição de tudo para um dicionário
    notes['total'] = total
    notes['maior'] = higher
    notes['menor'] = lower
    notes['média'] = total / len(num) # média entre todos os valores
    
    if sit == True:
        if notes['média'] > 7:
            notes['situação'] = 'ÓTIMA'
        elif 7 >= notes['média'] >= 6:
            notes['situação'] = 'BOA'
        elif 6 > notes['média'] >= 5:
            notes['situação'] = 'RAZOÁVEL'
        elif 5 > notes['média'] >= 4:
            notes['situação'] = 'RUIM'
        else:
            notes['situação'] = 'PÉSSIMA'
    return notes

note = funcNotes(5.5,2.5,10,6.5, sit=True)
print(note)