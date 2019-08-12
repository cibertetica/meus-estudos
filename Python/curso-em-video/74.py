# exercício 74
# maior e menor valores com tuplas

from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados são', end='')

for n in num:
    print(f' {n} |', end='')

print(f'O maior valor sorteado foi {max(num)}.')
print(f'O menor valor sorteado foi {min(num)}.')