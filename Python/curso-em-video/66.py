# exercício 66
# soma de diversos valores
# com flag executado pelo comando break
amount = total = 0
while True:
    n = int(input('Digite um número [ou 999 para parar]: '))
    if n == 999:
        break
    amount += 1 # amount = amount + 1 | quantos valores
    total += n # total = total + n | soma dos valores
print(f'Você digitou {amount} valores.\nA soma de todos os valores digitados é {total}.')