# exercício 64
# soma de diversos números informados
# e ignora o flag

n = c = total = 0

while n != 999:
    n = int(input('Digite um número: [999 para sair] '))
    total += n
    c += 1
print(f'Você digitou {c} números. A soma entre eles é {total - 999}')
print('Fim! ')