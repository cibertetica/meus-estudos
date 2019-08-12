# exercício 48 
# soma de números ímpares que são múltiplos de 3 e que se encontram entre 1 até 500

s = 0
n = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(c, end=" ")
        s += c
        n += 1
print(f'\nA soma dos {n} números solicitados é {s}. ')