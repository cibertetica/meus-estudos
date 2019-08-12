# exercício 65
# média e comparação de valores entre diversos números

from time import sleep

reply = 'S'
average = total = amount = higher = smaller = 0
# average -> média dos valores | total -> soma dos valores | amount -> quantidade de valores | higher -> número maior | smaller -> número menor

while reply != 'N':
    n = int(input('Digite um número: '))
    total += n # total = total + n
    amount += 1 # amount = amount + 1
    reply = input('Quer continuar? [S/N] ').upper()[0] # coloca em maiúsculas e lê apenas o primeiro caractere
    if amount == 1:
        higher = smaller = n
    else:
        if n > higher:
            higher = n
        if n < smaller:
            smaller = n
    while reply != 'S' and reply != 'N':
        print('Opção inválida!')
        reply = input('Quer continuar? [S/N] ').upper()[0]

average = float(total / amount)

print('Encerrada a contabilização.\nAnalisando os números...')
sleep(2)

print(f'''
Vamos as informações...
Você digitou {amount} valores.
A média dos valores digitados é {average:.2f}.
O maior valor é {higher}.
O menor valor é {smaller}.
'''
)