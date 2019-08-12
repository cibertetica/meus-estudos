# exercício 53
# identificar se uma frase é palíndroma
# palíndromo é uma frase que pode ser lida de trás para frente e permanece igual
# exemplos de frase:
# Apos a sopa
# A sacada da casa
# A torre da derrota
# O lobo ama o bolo
# Anotaram a data da maratona

phrase = input('Digite uma frase: ').strip().upper()
words = phrase.split()
joint = ''.join(words)
inverse = ''

for letter in range(len(joint) - 1, -1 , -1):
# o primeiro -1 corresponde da posição das letras na variável joint (0 a 19). São 20 letras, pegamos a posição - 1 pois o Python não contaria
# o segundo -1 corresponde a uma letra antes da primeira letra (0)
# o terceiro -1 é que vai voltando uma letra
    inverse = inverse + joint[letter]

if inverse == joint:
    print('\nA frase é palíndroma.')
else:
    print('\nA frase não é palíndroma.')

print(f'Frase digitada sem os espaços: {joint}')
print(f'Frase digitada de trás para frente: {inverse}')