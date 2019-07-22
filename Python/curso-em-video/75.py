# exercício 75 
# análise de dados com tupla

num = (int(input('Digite um número: ')) , int(input('Digite um número: ')) ,
        int(input('Digite um número: ')) , int(input('Digite um número: '))
)

print(f'Você digitou os valores \n{num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 foi o {num.index(3) + 1}º informado.')
else:
    print(f'O valor 3 não foi informado.')
print(f'Os valores pares digitados foram')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')