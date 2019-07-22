# exercício 77
# contando vogais em palavras

words = ('aprender' , 'programar' , 'linguagem' , 'curso', 'mercado')

for word in words:
    print(f'{word.upper()} -> ' , end=' ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter , end=' ')
    print('\n')