# criador de anagramas

from random import shuffle
from math import factorial

# palavra da qual vai se originar os anagramas
word = 'gol'
# transformar a palavra em uma lista para embaralhar cada letra
mix = list(word)
# quantos anagramas dá pra fazer com uma palavra? (com letras repetidas)
# é só calcular o fatorial do número de letras
anagram_amount = factorial(len(word))

print(f'A palavra {word} tem {anagram_amount} anagramas. \n')
print(f'Os anagramas são: \n')

for c in range(anagram_amount):
    shuffle(mix)
    anagram = ''.join(mix)
    print(f'{c + 1}º: {anagram}')
