# exercício 65 aperfeiçoado
# média e comparação de valores entre diversos números
# sem gambiarra; uso correto do break

from time import sleep

average = total = amount = higher = smaller = 0
# average -> média dos valores | total -> soma dos valores | amount -> quantidade de valores | higher -> número maior | smaller -> número menor

while True:
    n = int(input('Informe um número: '))
    amount += 1
    total += n

    if amount == 1:
        higher = smaller = n
    else:
        if n > higher:
            higher = n
        if n < smaller:
            smaller = n
   # tratamento de input
    while True:
        reply = input('Deseja continuar? [S/N] ').upper()[0]
        if reply in 'SN':
            break
        print('Opção inválida! Digite apenas S para sim ou N para não. ')

    if reply == 'N':
        break
    
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