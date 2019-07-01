# exercício 26 incrementado
# coloquei uma estrutura if para mudar a palavra 'vez' por 'vezes', seu plural, quando o número de ocorrências é maior que 1

phrase = input('Digite uma frase para ser analisada: ')

if phrase.count('A') > 1:
    print('A letra "A", em letra maiúscula, aparece', phrase.count('A') , 'vezes.')
else:
    print('A letra "A", em letra maiúscula, aparece', phrase.count('A') , 'vez.')
print('A primeira vez que a letra maiúscula "A" aparece é na posição' , (phrase.find('A') + 1))
print('A última vez que a letra maiúscula "A" aparece é na posição' , (phrase.rfind('A') + 1))