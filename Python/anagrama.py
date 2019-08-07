# criador de anagramas

from random import shuffle
from math import factorial

def anagram(word):
    anagrams = [] # lista onde serão armazenados todos os anagramas
    letters = list(word) # uma lista para separar cada letra da string
    anagram_amount = factorial(len(word)) # cálculo de quantos anagramas são possíveis para aquela palavra

    print(f'A palavra {word} tem {anagram_amount} anagramas possíveis.\n')
    print('Os anagramas são: ')

    while True:
        shuffle(letters)
        new_word = ''.join(letters)

        if new_word not in anagrams:
            anagrams.append(new_word)
        if len(anagrams) == anagram_amount:
            break

    for i, w in enumerate(anagrams):
        print(f'{i + 1}: {w}')

anagram('lua')        