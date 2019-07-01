# exercício 26
# Um programa que lê uma frase digitada pelo usuário e mostra:
# 1) quantas vezes aparece a letra "A"
# 2) Em que posição ela aparece na primeira vez
# 3) Em que posição ela aparece na última vez

phrase = input('Digite uma frase para ser analisada: ')

print('A letra "A", em letra maiúscula, aparece', phrase.count('A') , 'vez(es)')
print('A primeira vez que a letra maiúscula "A" aparece é na posição' , (phrase.find('A') + 1))
print('A última vez que a letra maiúscula "A" aparece é na posição' , (phrase.rfind('A') + 1))