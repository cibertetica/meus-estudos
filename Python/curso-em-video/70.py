# exercício 70
# análise de produtos comprados
# pessoa informa quantos produtos comprou, o programa retorna o total das compras, quantos produtos custam mais de R$ 1.000,00 e o produto mais barato e seu valor

from time import sleep
total = amount = amount_higher_price = lower_price = lower_product = 0
# continue_register = ''
# total -> soma | amount -> quantidade de produtos | amount_higher_price -> qnt de produtos com o preço mais alto | lower_price -> preço mais baixo | lower_product -> o nome do produto com preço mais baixo

while True: 
    product = input('Descrição do Produto: ').title()
    price = float(input('Preço: R$ '))
    amount += 1
    total += price # soma dos produtos
    if price >= 1000:
        amount_higher_price += 1
    if amount == 1 or price < lower_price: # simplificação de um if-else 
        lower_price = price
        lower_product = product

    # continuar registrando produtos? 
    continue_register = input('Quer continuar? [S/N] ').upper().strip()[0]
    while continue_register != 'S' and continue_register != 'N': # verificação
        print('Opção inválida!')
        continue_register = input('Quer continuar? [APENAS S para sim ou N para não] ').upper().strip()[0]
    if continue_register == 'N':
        break

print('Contabilizando seus produtos...')
sleep(1.5)
print(f''' 
O total das suas compras é R$ {total:.2f}.
Você comprou {amount_higher_price} produto(s) que custa(m) mais de R$ 1000,00.
{lower_product}, que custa R$ {lower_price:.2f}, é o produto mais barato da sua lista.
'''
)