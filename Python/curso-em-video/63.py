# exercício 63
# sequência de fibonacci
# sequência começando por 0 e 1 em que cada termo subsequente corresponde a soma dos dois anteriores

print('Sequência de Fibonacci\n' , '-' * 18)
terms = int(input('Quantos termos você quer mostrar? '))
first = 0
second = 1
print(f'{first} -> {second} -> ', end='')
c = 3
while c <= terms:
    next_n = first + second
    first = second
    second = next_n
    print(f'{next_n} -> ' , end='')
    c += 1