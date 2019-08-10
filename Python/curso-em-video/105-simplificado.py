# exercício 105 simplificado
# função que gera dicionário com total, média, nota maior e menor através de um número ilimitado de notas

def funcNotes(*num):
    notes = {}
    notes['total'] = sum(num)
    notes['maior'] = max(num)
    notes['menor'] = min(num)
    notes['média'] = sum(num) / len(num)
    return notes

note = funcNotes(5, 7, 7.5, 10)
print(note)